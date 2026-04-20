from fastapi import FastAPI

app = FastAPI(title="Agentic ALM Framework")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process-insight")
def process_insight(payload: dict):
    return {
        "message": "Insight received",
        "flow": "Adapter -> Planner -> Approval -> Execution"
    }