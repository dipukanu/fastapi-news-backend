from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import secrets

from app.database.session import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate

router = APIRouter(prefix="/api/v1/clients", tags=["Clients"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Register a new API client",
)
def register_client(payload: ClientCreate, db: Session = Depends(get_db)):
    """
    Registers a new client with a name and optional description,
    and returns the generated client_id and client_secret.
    """
    client_id = secrets.token_hex(8)
    client_secret = secrets.token_urlsafe(32)

    if db.query(Client).filter_by(client_id=client_id).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client ID collision—please retry",
        )

    client = Client(
        client_id=client_id,
        client_secret=client_secret,
        name=payload.name,
        description=payload.description,
    )
    db.add(client)
    db.commit()
    db.refresh(client)

    return {"client_id": client.client_id, "client_secret": client.client_secret}
