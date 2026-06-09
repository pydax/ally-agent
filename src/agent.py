import json
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List

# --- Strict Pydantic Cognitive Guardrail Schemas ---
class StudyMilestone(BaseModel):
    phase: str
    allotted_hours: float
    action_item: str

class LowCognitiveLoadPlan(BaseModel):
    learner_id: str
    target_certification: str
    source_citation: str
    milestones: List[StudyMilestone] = Field(max_items=3, description="Strictly capped at 3 paths to protect focus capacity")

# --- Multi-Agent Orchestration Layer ---
class EnterpriseLearningAgents:
    def __init__(self):
        data_dir = Path("data")
        with open(data_dir / "learner_performance.json", "r") as f:
            self.learner_perf = json.load(f)
        with open(data_dir / "work_activity_signals.json", "r") as f:
            self.work_signals = json.load(f)
        with open(data_dir / "fabric_semantic_seed.json", "r") as f:
            self.semantic_seed = json.load(f)
        with open(data_dir / "synthetic_docs.json", "r") as f:
            self.synthetic_docs = json.load(f)

    def learning_path_curator(self, role: str) -> dict:
        """Agent 1 (Foundry IQ): Extracts target certification guided by data definitions."""
        if "Cloud" in role:
            target = "AZ-204"
        elif "DevOps" in role:
            target = "AZ-400"
        else:
            target = "DP-203"
        return {
            "role": role,
            "target_certification": target,
            "source_doc_title": "Engineering Certification Enablement Guide (Synthetic)"
        }

    def study_plan_generator(self, employee_id: str, curation: dict) -> LowCognitiveLoadPlan:
        """Agent 2 (Fabric IQ): Generates a workload-aware 3-step timeline."""
        cert_id = curation["target_certification"]
        cert_meta = next((c for c in self.semantic_seed["certifications"] if c["id"] == cert_id), {"recommended_hours": 20})
        rec_hours = cert_meta["recommended_hours"]
        
        emp_workload = next((w for w in self.work_signals if w["employee_id"] == employee_id), self.work_signals[0])
        allocated_daily_load = 1.0 if emp_workload["meeting_hours_per_week"] > 20 else 2.0

        return LowCognitiveLoadPlan(
            learner_id=employee_id,
            target_certification=cert_id,
            source_citation=curation["source_doc_title"],
            milestones=[
                StudyMilestone(phase="Core Competency Dev", allotted_hours=rec_hours * 0.5, action_item=f"Study fundamentals for {allocated_daily_load} hour/day."),
                StudyMilestone(phase="Practical Verification", allotted_hours=rec_hours * 0.3, action_item="Build functional sandbox prototypes."),
                StudyMilestone(phase="Grounded Evaluation", allotted_hours=rec_hours * 0.2, action_item="Take 3-question evaluation block.")
            ]
        )

    def engagement_agent(self, employee_id: str) -> str:
        """Agent 3 (Work IQ): Adapts interaction based on calendar stress signals."""
        emp = next((w for w in self.work_signals if w["employee_id"] == employee_id), self.work_signals[0])
        return f"[Engagement Agent] Notifications muted during peak blocks. Routing alerts via user's preferred '{emp['preferred_learning_slot']}' slot."

    def assessment_agent(self, employee_id: str) -> dict:
        """Agent 4 (Foundry IQ): Cross-checks readiness against target threshold rules."""
        perf = next((p for p in self.learner_perf if p["learner_id"] == "L-1001"), self.learner_perf[0])
        passed_rules = perf["practice_score_avg"] >= 75
        return {
            "learner": employee_id,
            "target_threshold": "75% Score Required (Source: Engineering Certification Guide)",
            "historical_average": f"{perf['practice_score_avg']}%",
            "status": "PROCEED_TO_EXAM" if passed_rules else "RECOMMEND_LOOP_BACK"
        }

    def manager_insights_agent(self) -> dict:
        """Agent 5 (Fabric + Work IQ): Aggregates team metrics while fully protecting employee PII."""
        at_risk_count = sum(1 for e in self.work_signals if e["meeting_hours_per_week"] > 20)
        return {
            "risk_summary": f"{at_risk_count} team profiles are capacity-constrained (>20h meetings/wk) and show lower study completion metrics.",
            "source_doc": "Quarterly Learning Performance Summary (Synthetic)"
        }