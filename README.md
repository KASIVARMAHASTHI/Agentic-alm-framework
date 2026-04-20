# Agentic ALM Framework

Agentic ALM Framework is a modular, production-oriented framework designed to convert analytical insights into governed, executable actions.

## 🚀 Production Features Added
- Async execution with queue + worker
- Retry mechanism
- Persistence (file-based DB)
- Workflow status tracking API
- LLM + fallback planning
- Dockerized deployment

---

## 🐳 Run with Docker

### Build and run
```bash
docker-compose up --build
```

### Access API
- http://localhost:8000/docs

---

## 🧪 Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🔄 Full Architecture

```text
Insight
 → Adapter
 → LLM Planner
     ↳ fallback → Catalog
 → Approval
 → Queue
 → Worker
 → Retry
 → Execution
 → Audit
 → Persistence
```

---

## 📡 APIs
- `POST /process-insight`
- `GET /status/{correlation_id}`
- `GET /health`

---

## 💡 Why this matters
This project demonstrates a production-style system combining:
- AI decisioning
- backend system design
- async processing
- workflow lifecycle management

---

## 🔮 Next Enhancements
- Replace file DB with PostgreSQL
- Add Redis/Kafka queue
- Add authentication
- Add UI for approvals
