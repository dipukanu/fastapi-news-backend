import logging

from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timedelta

from app.database.session import get_db
from app.models.client import Client
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/api/v1/token")
def generate_token(
    client_id: str = Form(...),
    client_secret: str = Form(...),
    db: Session = Depends(get_db),
):
    client = db.query(Client).filter_by(client_id=client_id).first()
    if not client or client.client_secret != client_secret:
        raise HTTPException(status_code=401, detail="Invalid client credentials")

    expires = datetime.utcnow() + timedelta(minutes=60)
    payload = {
        "sub": client.client_id,
        "exp": expires,
    }
    token = jwt.encode(payload, settings.client_secret, algorithm="HS256")

    logger.info(f"Access token generated successfully for client_id: {client_id}")

    return {"access_token": token, "token_type": "bearer"}
