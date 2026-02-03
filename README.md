<<<<<<< HEAD
# honeypot-api
Agentic Honeypot API to detect scam messages and extract intelligence.
=======
# Honeypot API

**Agentic Honey-Fix API** built with FastAPI to detect scam messages, extract intelligence, and calculate risk levels.  
This API is designed for hackathon evaluation and supports API key authentication.

---

## Features

- POST `/analyze` endpoint
- Extracts:
  - Phone numbers
  - Emails
  - URLs
- Calculates scam risk level (`HIGH` / `LOW`)
- API key protected (`x-api-key = HONEYFIX-1234`)
- Swagger documentation available at `/docs`
- Ready for public deployment (Render, Railway, etc.)

---

## Quick Start (Local)

1. Clone the repository:

```bash
git clone https://github.com/<username>/honeypot-api.git
cd honeypot-api
>>>>>>> 75c0cec (Initial commit - Honeypot API ready)
