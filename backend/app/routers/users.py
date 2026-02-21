from fastapi import APIRouter, Depends, Header, HTTPException

from app.core.rbac import assert_permission
from app.schemas.auth import CreateUserRequest
from app.services.auth_service import create_user

router = APIRouter(prefix="/users", tags=["users"])


def role_guard(x_role: str = Header(default="team_member")) -> str:
    if not x_role:
        raise HTTPException(status_code=401, detail="Missing role header")
    return x_role


@router.post("")
def create_platform_user(payload: CreateUserRequest, role: str = Depends(role_guard)):
    assert_permission(role, "users.manage")
    return create_user(payload.model_dump())
