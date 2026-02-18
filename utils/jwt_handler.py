from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

SECRET_KEY = "your-secret-key-change-this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7


def create_tokens(user_id: int, email: str) -> dict:
    """Create access and refresh tokens for a user."""
    now = datetime.now(timezone.utc)

    access_payload = {
        "sub": str(user_id),
        "email": email,
        "type": "access",
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    access_token = jwt.encode(access_payload, SECRET_KEY, algorithm=ALGORITHM)

    refresh_payload = {
        "sub": str(user_id),
        "email": email,
        "type": "refresh",
        "exp": now + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    }
    refresh_token = jwt.encode(refresh_payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


def verify_token(token: str, token_type: str = "access") -> dict | None:
    """Verify a JWT token and return its payload, or None if invalid."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != token_type:
            return None
        return payload
    except JWTError:
        return None
