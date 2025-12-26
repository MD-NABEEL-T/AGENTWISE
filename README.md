# AI Rule Assistant – Backend

This repository contains the FastAPI backend used for AI-powered rule retrieval,
integrated with Appian using OpenAPI.

## Tech Stack
- Python (FastAPI)
- OpenAPI 3.1
- Appian Integration
- ngrok (temporary public URL)

## API Endpoint

POST /get-rule

### Request Body
```json
{
  "claimType": "Flood",
  "state": "Florida"
}
Response
{
  "summary": "Flood claims in Florida must be reported within 30 days.",
  "document": "FloodPolicy.pdf",
  "page": 2
}

Appian Integration

OpenAPI imported into Appian Connected System

Expression Rule calls integration

Response used inside Appian UI and workflows

Demo Evidence

Screenshots included showing:

FastAPI Swagger UI

ngrok public URL

Appian integration test success
