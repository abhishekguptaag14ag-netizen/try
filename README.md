# OmniCore Platform

Production-grade multi-tenant **CMS + CRM + LMS + HRMS + Accounting** foundation for a marketing + training company.

## Highlights
- Private controlled onboarding (no public signup)
- Multi-tenant isolation with strict RBAC
- WhatsApp + call-first CRM flows
- LMS + HR + accounting in one event-audited system
- API-first backend and modular deployment topology

## Repository structure
- `db/schema.sql` - relational schema for core modules
- `docs/architecture.md` - backend flow, frontend pages, security, deployment
- `docs/permission-matrix.md` - role-level feature access matrix
- `docs/api-overview.md` - endpoint map by module
- `backend/` - FastAPI service scaffold with auth + tenant guard + RBAC
- `frontend/` - route and UI composition blueprint
- `infra/` - Docker Compose for local environments

## Quick start (backend)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Product principles
1. **Tenant safety first**: every mutable table carries `tenant_id`; super admin can cross-tenant read by explicit scope.
2. **Audit everything**: create/update/delete, auth events, impersonation, payroll calculations, and financial postings.
3. **Modular domains**: communication, CRM, LMS, HRMS, accounting, and platform governance.
4. **Feature flags + usage caps**: super admin can turn modules on/off and cap quotas per tenant.
