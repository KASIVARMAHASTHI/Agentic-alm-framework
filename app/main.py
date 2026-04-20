from fastapi import FastAPI

from app.adapter.service import AdapterService
from app.planner.service import PlannerService
from app.planner.llm_planner import LLMPlannerService
from app.approvals.service import ApprovalService
from app.executor.service import ExecutionService
from app.audit.service import AuditService
from app.models.contracts import InsightRequest
from app.status.service import StatusService

app = FastAPI(title="Agentic ALM Framework")

adapter = AdapterService()
planner = PlannerService()
llm_planner = LLMPlannerService()
approval = ApprovalService()
executor = ExecutionService()
audit = AuditService()
status_service = StatusService()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/status/{correlation_id}")
def get_status(correlation_id: str):
    return status_service.get_status(correlation_id)


@app.post("/process-insight")
def process_insight(request: InsightRequest):
    request_dict = request.dict()
    correlation_id = request_dict.get("correlation_id", "unknown")

    # Step 1: Persist initial request
    status_service.create_workflow(request_dict)

    # Step 2: Normalize input
    normalized = adapter.normalize(request_dict)

    # Step 3: LLM-based planning attempt
    plan = llm_planner.create_plan(normalized)

    # Step 4: Fallback to catalog planner if needed
    if not plan or "plan" not in plan:
        plan = planner.create_plan(normalized)

    # Step 5: Approval decision
    approval_required = approval.requires_approval(plan)

    if approval_required:
        status_service.update_status(correlation_id, "approval_pending")
        audit_log = audit.log({
            "stage": "approval",
            "status": "pending",
            "plan": plan
        })
        return {
            "status": "approval_required",
            "plan": plan,
            "audit": audit_log
        }

    # Step 6: Queue execution
    execution_result = executor.execute(plan)
    status_service.update_status(correlation_id, "queued")

    # Step 7: Audit
    audit_log = audit.log({
        "stage": "execution",
        "status": execution_result["execution_status"],
        "details": execution_result
    })

    return {
        "status": "queued",
        "plan": plan,
        "execution": execution_result,
        "audit": audit_log
    }
