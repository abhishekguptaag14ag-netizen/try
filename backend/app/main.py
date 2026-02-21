from fastapi import FastAPI

from app.core.config import settings
from app.middleware.tenant import tenant_context_middleware
from app.routers import auth, leads, users

app = FastAPI(title=settings.app_name)
app.middleware("http")(tenant_context_middleware)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(leads.router, prefix="/api/v1")


@app.get("/health")
def healthcheck():
    return {"status": "ok"}
