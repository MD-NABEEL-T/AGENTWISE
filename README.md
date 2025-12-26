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
