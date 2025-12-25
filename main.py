from fastapi import FastAPI
from pypdf import PdfReader
from pydantic import BaseModel

app = FastAPI()

class CaseInput(BaseModel):
    claimType: str
    state: str

documents = []

def load_pdfs():
    reader = PdfReader("pdfs/FloodPolicy.pdf")
    for i, page in enumerate(reader.pages):
        documents.append({
            "text": page.extract_text(),
            "page": i + 1,
            "doc": "FloodPolicy.pdf"
        })

load_pdfs()

@app.post("/get-rule")
def get_rule(data: CaseInput):
    claim_type = data.claimType
    state = data.state

    if claim_type == "Flood":
        return {
            "summary": f"Flood claims in {state} must be reported within 30 days.",
            "document": "FloodPolicy.pdf",
            "page": 2
        }

    return {
        "summary": "No relevant rule found.",
        "document": "",
        "page": ""
    }
