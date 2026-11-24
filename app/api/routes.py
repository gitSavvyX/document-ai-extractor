from fastapi import APIRouter, HTTPException
from app.models.schemas import ExtractionRequest, InvoiceData
from app.services.extractor import extract_invoice_data

router = APIRouter()

@router.post("/extract", response_model=InvoiceData, summary="Extract data from invoice text")
async def extract_document(request: ExtractionRequest):
    try:
        # We pass the raw text to the AI service
        extracted_data = extract_invoice_data(request.raw_text)
        return extracted_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction failed: {str(e)}")
