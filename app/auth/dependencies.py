from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")


def get_current_client(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, settings.client_secret, algorithms=["HS256"])
        client_id = payload.get("sub")
        if not client_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload"
            )
        return client_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
