import json
from openai import OpenAI
from app.core.config import get_settings
from app.models.schemas import InvoiceData

settings = get_settings()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def extract_invoice_data(raw_text: str) -> InvoiceData:
    """Uses OpenAI JSON mode to extract structured data from text."""
    
    system_prompt = """
    You are an AI Document Intelligence Agent. 
    Your job is to extract invoice details from the provided raw text.
    You must respond with a valid JSON object that strictly follows this schema:
    {
        "invoice_number": "string",
        "vendor_name": "string",
        "date": "YYYY-MM-DD",
        "total_amount": float,
        "line_items": [
            {
                "description": "string",
                "quantity": int,
                "unit_price": float,
                "total_price": float
            }
        ]
    }
    If a value is missing, guess it or use null. Do not include markdown formatting like ```json.
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview", # Or gpt-3.5-turbo
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Extract the data from this text:\n{raw_text}"}
        ]
    )
    
    json_response = json.loads(response.choices[0].message.content)
    return InvoiceData(**json_response)
