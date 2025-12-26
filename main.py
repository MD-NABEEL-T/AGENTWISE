from fastapi import FastAPI
from pypdf import PdfReader
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI",
    version="0.1.0",
    servers=[
        {
            "url": "https://unconned-overhumane-omer.ngrok-free.dev",
            "description": "Ngrok public URL"
        }
    ]
)


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
    if data.claimType == "Flood":
        return {
            "summary": f"Flood claims in {data.state} must be reported within 30 days.",
            "document": "FloodPolicy.pdf",
            "page": 2
        }

    return {
        "summary": "No relevant rule found.",
        "document": "",
        "page": ""
    }
