from app.core.security import create_access_token, hash_password, verify_password

FAKE_USERS = {
    "head": {
        "id": "u-super-1",
        "tenant_id": None,
        "role": "super_admin",
        "username": "head",
        "email": "head@omnicore.local",
        "password_hash": hash_password("ChangeMe123!"),
    }
}


def login(identity: str, password: str) -> str | None:
    user = next(
        (u for u in FAKE_USERS.values() if identity in (u["username"], u["email"])),
        None,
    )
    if not user or not verify_password(password, user["password_hash"]):
        return None
    return create_access_token(user["id"], user["tenant_id"], user["role"])


def create_user(payload: dict) -> dict:
    user_id = f"u-{len(FAKE_USERS) + 1}"
    user = {
        "id": user_id,
        "tenant_id": payload["tenant_id"],
        "role": payload["role"],
        "username": payload["username"],
        "email": payload["email"],
        "password_hash": hash_password(payload["password"]),
    }
    FAKE_USERS[user_id] = user
    return user
