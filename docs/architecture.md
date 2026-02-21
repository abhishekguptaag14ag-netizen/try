# OmniCore Architecture (CMS + CRM + LMS + HRMS + Accounting)

## 1) Backend logic flow
1. **Authentication**: username/email + password with optional OTP challenge (WhatsApp/SMS provider abstraction).
2. **Token issue**: JWT includes `sub`, `role`, and `tenant_id` (unless super admin).
3. **Request guard chain**:
   - Resolve tenant context (`X-Tenant-ID` header or token claim).
   - Check module feature flag and tenant limits.
   - Authorize via RBAC permission map.
   - Persist audit log entry on mutations.
4. **Domain orchestration**:
   - Communication events create/update contacts and leads.
   - Lead stage transitions trigger tasks and reminders.
   - Conversion to client/student links to invoice/enrollment workflow.
   - Payroll and accounting post journal entries.

## 2) Module boundaries
- **Platform Core**: tenants, users, roles, permissions, limits, flags, impersonation.
- **Communication**: WhatsApp accounts, threads, messages, call logs, templates, broadcasts.
- **CRM**: contacts, leads, pipelines, tasks, follow-ups, conversion.
- **HRMS**: attendance, work logs, salary plans, payroll runs, payslips.
- **LMS**: courses, batches, enrollments, progress.
- **Accounting**: invoices, payments, expenses, journal entries, P&L views.

## 3) Frontend page structure
- `/login`
- `/super-admin`
  - `/tenants`
  - `/tenants/:id/limits`
  - `/feature-flags`
  - `/impersonation`
  - `/global-analytics`
- `/dashboard` (role-aware widgets)
- `/communication`
  - `/whatsapp/inbox`
  - `/whatsapp/templates`
  - `/whatsapp/broadcasts`
  - `/calls/logs`
- `/crm`
  - `/leads`
  - `/pipelines`
  - `/tasks`
  - `/contacts`
- `/team`
  - `/members`
  - `/attendance`
  - `/performance`
  - `/payroll`
- `/lms`
  - `/courses`
  - `/batches`
  - `/students`
  - `/progress`
- `/accounting`
  - `/invoices`
  - `/payments`
  - `/expenses`
  - `/reports`

## 4) Security considerations
- Strong password hashing (bcrypt/argon2 preferred)
- MFA support for privileged roles
- Tenant isolation enforced in ORM policies + SQL predicates
- PII and tokens encrypted at rest
- Signed webhook verification (WhatsApp/call providers)
- Immutable audit logs + impersonation event tagging
- Rate limiting and brute-force protection on auth
- Least-privilege service accounts and secret manager usage

## 5) Backup and resilience
- Daily full DB backup + 15-minute WAL archiving
- Object storage versioning for recordings/documents
- Disaster recovery playbook (RPO: 15m, RTO: 2h)
- Queue-based retry workers for webhook ingestion and broadcasts

## 6) Deployment-ready structure
- **API**: FastAPI service (horizontal scaling)
- **Workers**: async queue consumers for messaging and scheduled jobs
- **DB**: PostgreSQL with read replica option
- **Cache/Queue**: Redis
- **Storage**: S3-compatible blob storage
- **Ingress**: Nginx or cloud load balancer + TLS
- **Observability**: OpenTelemetry traces + Prometheus/Grafana + centralized logs
