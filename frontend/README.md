# Frontend Blueprint

Recommended stack: **Next.js + TypeScript + Tailwind + TanStack Query + Zustand**.

## UI principles
- Single-screen workflows for non-technical users
- Minimal clicks (drawer-based create forms)
- Mobile-first tables with card fallback
- Light/dark mode toggles

## Core layout
- App shell with role-aware left navigation
- Top bar with global search, notifications, attendance timer, profile
- Dashboard widgets injected from `/api/v1/dashboard/{role}`

## Shared components
- `TenantScopeBadge`
- `PermissionGate`
- `KanbanPipeline`
- `ChatPanel`
- `CallDialer`
- `InvoiceComposer`
- `AttendanceClock`
