from pydantic import BaseModel, Field
from typing import List

class LineItem(BaseModel):
    description: str = Field(description="Description of the product or service")
    quantity: int = Field(description="Number of items purchased")
    unit_price: float = Field(description="Price per unit")
    total_price: float = Field(description="Total price for this line item")

class InvoiceData(BaseModel):
    invoice_number: str = Field(description="Unique invoice identifier")
    vendor_name: str = Field(description="Name of the company issuing the invoice")
    date: str = Field(description="Date of the invoice (YYYY-MM-DD)")
    total_amount: float = Field(description="Total amount due")
    line_items: List[LineItem] = Field(description="List of items in the invoice")

class ExtractionRequest(BaseModel):
    raw_text: str = Field(description="The raw unstructured text from the invoice")
