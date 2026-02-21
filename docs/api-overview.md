# API Endpoints Overview (`/api/v1`)

## Auth
- `POST /auth/login` - username/email + password login
- `POST /auth/login/otp/verify` - optional OTP completion
- `POST /auth/impersonate` - super admin scoped impersonation token

## Platform Admin
- `POST /tenants`
- `GET /tenants`
- `PATCH /tenants/{tenant_id}`
- `PUT /tenants/{tenant_id}/limits`
- `PUT /tenants/{tenant_id}/features/{feature_key}`
- `POST /users`
- `PATCH /users/{user_id}/disable`

## Communication
- `POST /communication/whatsapp/webhooks`
- `GET /communication/whatsapp/threads`
- `POST /communication/whatsapp/threads/{thread_id}/messages`
- `POST /communication/whatsapp/broadcasts`
- `POST /communication/calls/click-to-call`
- `GET /communication/calls/logs`

## CRM
- `POST /crm/leads`
- `GET /crm/leads`
- `PATCH /crm/leads/{lead_id}/stage`
- `POST /crm/leads/{lead_id}/followups`
- `POST /crm/contacts`
- `POST /crm/conversions/{lead_id}/client`

## HRMS
- `POST /hr/attendance/login`
- `POST /hr/attendance/logout`
- `PATCH /hr/attendance/{log_id}/override`
- `POST /hr/payroll/runs`
- `POST /hr/payroll/runs/{run_id}/approve`
- `GET /hr/payslips/{user_id}`

## LMS
- `POST /lms/courses`
- `POST /lms/batches`
- `POST /lms/enrollments`
- `PATCH /lms/enrollments/{enrollment_id}/progress`
- `GET /lms/students/{student_id}/dashboard`

## Accounting
- `POST /accounting/invoices`
- `POST /accounting/payments`
- `POST /accounting/expenses`
- `GET /accounting/reports/profit-loss`
- `GET /accounting/reports/collections`
