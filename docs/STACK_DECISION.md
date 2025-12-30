STACK DECISION (FROZEN)

Frontend:
- React
- TypeScript
- Browser-first SPA

Backend:
- Python
- FastAPI
- Single-process internal service

Constraints:
- Backend implementation in Node.js or TypeScript is prohibited.
- Any previously generated backend code using Node.js is non-authoritative.

Rationale:
- AI tooling density
- Local execution friendliness
- Future desktop packaging compatibility

Stage 6 Capability Support:
- Persistence: Supported via Python database libraries (implementation choice at Stage 6)
- External API calls: Supported via Python HTTP clients (requests, httpx, etc.)
- Background tasks: Supported via Python async/await, task queues, or scheduling libraries (implementation choice at Stage 6)

Note: This stack decision defines the technology foundation only. Specific implementation libraries (database, task queue, etc.) are chosen during Stage 6 implementation, not at stack decision time.