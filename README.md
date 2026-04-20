# Agentic ALM Framework

Agentic ALM Framework is a modular framework for turning analytical insights into governed, executable workflows. Instead of stopping at dashboards, alerts, or recommendations, this project focuses on the full action lifecycle: intake, planning, approval, execution, auditability, persistence, and deployment readiness.

## Why this project exists
Many analytics systems are good at generating signals but weak at operationalizing them. This framework is designed to bridge that gap by introducing a controlled, extensible path from insight to action.

## What this framework does
- Accepts structured insight payloads from upstream systems
- Normalizes requests through an adapter layer
- Generates context-aware action plans
- Uses an LLM-style planner with a safe catalog fallback strategy
- Routes risky steps for approval
- Queues execution for asynchronous processing
- Applies retry logic for resiliency
- Tracks workflow state through persistence and status APIs
- Supports containerized deployment

## Key architecture highlights
- **Adapter Layer** for canonical payload normalization
- **Planner Layer** for dynamic and fallback-based action planning
- **Approval Layer** for human-in-the-loop control of risky actions
- **Execution Layer** with queue, worker, and retry handling
- **Audit Layer** for lifecycle logging and traceability
- **Persistence Layer** for workflow state tracking
- **Deployment Layer** using Docker and Docker Compose

## End-to-end lifecycle
```text
Insight
 → Adapter
 → LLM Planner
     ↳ fallback → Catalog Planner
 → Approval
 → Queue
 → Worker
 → Retry
 → Execution
 → Audit
 → Persistence
 → Status Tracking
```

## Current capabilities
- Dynamic action catalog based on insight type and severity
- Simulated LLM-assisted planning with deterministic fallback
- Async execution model using queue and worker pattern
- Retry wrapper for resilient execution
- File-backed persistence for workflow state
- Status lookup by correlation ID
- Dockerized local deployment

## API endpoints
- `GET /health` — service health check
- `POST /process-insight` — ingest and process insight requests
- `GET /status/{correlation_id}` — fetch workflow status

## Example use cases
- Inventory threshold breach response
- Risk-control workflow execution
- Operational alert handling with approvals
- Policy-driven enterprise actions
- Human-in-the-loop action lifecycle automation

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run with Docker
```bash
docker-compose up --build
```

Then open:
- `http://localhost:8000/docs`

## Tech stack
- Python
- FastAPI
- Pydantic
- Docker

## Why this is a strong engineering project
This project is intentionally built as a framework rather than a one-off demo. It combines backend service design, workflow orchestration, fallback-driven AI patterns, asynchronous execution, and production-oriented deployment setup in a single architecture.

## Planned next steps
- Replace file-based persistence with PostgreSQL
- Introduce Redis or Kafka for production-grade queuing
- Add authentication and tenant-aware controls
- Add approval UI or chatbot interface
- Add observability metrics and structured logging
