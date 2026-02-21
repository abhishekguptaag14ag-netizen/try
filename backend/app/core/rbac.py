from fastapi import HTTPException, status

ROLE_PERMISSIONS = {
    "super_admin": {"*"},
    "admin": {
        "users.manage",
        "crm.manage",
        "communication.manage",
        "hr.manage",
        "lms.manage",
        "accounting.manage",
    },
    "manager": {
        "crm.manage",
        "communication.manage",
        "tasks.manage",
        "team.view",
    },
    "team_member": {
        "communication.reply",
        "crm.update",
        "tasks.update",
        "attendance.self",
    },
    "student": {"lms.self", "payments.self"},
    "client": {"crm.self", "invoices.self", "payments.self"},
}


def assert_permission(role: str, permission: str) -> None:
    allowed = ROLE_PERMISSIONS.get(role, set())
    if "*" in allowed or permission in allowed:
        return
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=f"Role '{role}' lacks permission '{permission}'",
    )
