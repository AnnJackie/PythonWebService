from pydantic import BaseModel


class AuthResponse(BaseModel):
    jwt: str