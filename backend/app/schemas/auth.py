from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    identity: str
    password: str
    otp: str | None = None


class CreateUserRequest(BaseModel):
    tenant_id: str | None
    role: str
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
