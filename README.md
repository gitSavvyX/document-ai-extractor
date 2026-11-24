# 📄 Document AI Extractor Microservice

A production-grade FastAPI microservice that processes unstructured business documents (invoices, receipts) and extracts structured JSON data using Large Language Models (LLMs). 

## 🏗️ Architecture
This project is built using a modular microservice architecture:
• **API Layer (`app/api`)**: Handles HTTP requests and routes.
• **Core Config (`app/core`)**: Manages environment variables and settings.
• **Data Schemas (`app/models`)**: Uses Pydantic for strict data validation and structured LLM outputs.
• **Services (`app/services`)**: Contains the business logic for AI extraction and mock database storage.

## 🛠️ Tech Stack
| Category | Technologies |
| :--- | :--- |
| Backend Framework | FastAPI, Uvicorn |
| AI & LLM | OpenAI API (JSON Mode), Prompt Engineering |
| Data Validation | Pydantic |
| Database | SQLite (via Python SQLAlchemy) |
| DevOps | Docker, Pytest |

## ⚙️ Endpoints
• `GET /` : Health check.
• `POST /api/v1/extract` : Accepts raw text, extracts data, and returns strict JSON.

## 🚀 Running the Project
1. Build the Docker image: `docker build -t document-ai-extractor .`
2. Run the container: `docker run -p 8000:8000 --env-file .env document-ai-extractor`
3. Access the API docs at `http://localhost:8000/docs`
