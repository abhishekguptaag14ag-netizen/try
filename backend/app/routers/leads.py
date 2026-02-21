from fastapi import APIRouter, Depends, Header

from app.core.rbac import assert_permission

router = APIRouter(prefix="/crm/leads", tags=["crm"])


@router.get("")
def list_leads(x_role: str = Header(default="manager")):
    assert_permission(x_role, "crm.manage")
    return {
        "items": [
            {"id": "lead-1", "name": "Inbound WhatsApp Lead", "stage": "new"},
            {"id": "lead-2", "name": "Call Campaign Lead", "stage": "follow_up"},
        ]
    }
