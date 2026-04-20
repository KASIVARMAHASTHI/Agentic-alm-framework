from fastapi import FastAPI

from app.adapter.service import AdapterService
from app.planner.service import PlannerService
from app.planner.llm_planner import LLMPlannerService
from app.approvals.service import ApprovalService
from app.executor.service import ExecutionService
from app.audit.service import AuditService
from app.models.contracts import InsightRequest

app = FastAPI(title="Agentic ALM Framework")

adapter = AdapterService()
planner = PlannerService()
llm_planner = LLMPlannerService()
approval = ApprovalService()
executor = ExecutionService()
audit = AuditService()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/process-insight")
def process_insight(request: InsightRequest):
    # Step 1: Normalize input
    normalized = adapter.normalize(request.dict())

    # Step 2: LLM-based planning attempt
    plan = llm_planner.create_plan(normalized)

    # Step 3: Fallback to catalog planner if needed
    if not plan or "plan" not in plan:
        plan = planner.create_plan(normalized)

    # Step 4: Approval decision
    approval_required = approval.requires_approval(plan)

    if approval_required:
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

    # Step 5: Execute
    execution_result = executor.execute(plan)

    # Step 6: Audit
    audit_log = audit.log({
        "stage": "execution",
        "status": execution_result["execution_status"],
        "details": execution_result
    })

    return {
        "status": "completed",
        "plan": plan,
        "execution": execution_result,
        "audit": audit_log
    }
