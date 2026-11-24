from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Enterprise Document AI Microservice for Invoice Extraction"
)

# CORS setup for production readiness
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "online", "project": settings.PROJECT_NAME}


from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/ui")
def serve_ui():
    return FileResponse("app/static/index.html")
