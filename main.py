from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from database import create_document, db
from schemas import Contact, QuoteRequest, Booking, Subscription

app = FastAPI(title="AgriForce Robotics API", version="1.0.0")

# CORS - allow all for demo; in production, restrict to your domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "name": "AgriForce Robotics API"}


@app.get("/test")
def test_db():
    try:
        if db is None:
            raise Exception("Database not initialized")
        # Attempt a simple command
        db.command("ping")
        return {"database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Forms and lead capture endpoints
@app.post("/api/contact")
def submit_contact(payload: Contact):
    try:
        doc_id = create_document("contact", payload)
        return {"ok": True, "id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/quote")
def submit_quote(payload: QuoteRequest):
    try:
        doc_id = create_document("quoterequest", payload)
        return {"ok": True, "id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/book-visit")
def submit_booking(payload: Booking):
    try:
        doc_id = create_document("booking", payload)
        return {"ok": True, "id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/subscribe")
def subscribe(payload: Subscription):
    try:
        doc_id = create_document("subscription", payload)
        return {"ok": True, "id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
