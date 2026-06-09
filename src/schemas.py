from pydantic import BaseModel
from typing import List

class CurationOutput(BaseModel):
    role: str
    target_certification: str
    source_doc_title: str
    grounded_text_snippet: str
    iq_layer_applied: str

class MilestoneSchema(BaseModel):
    milestone_step: int
    target_hours: float
    cognitive_load_cap: str

class ReasoningMetadataSchema(BaseModel):
    planner_strategy: str
    critic_audit: str
    cognitive_buffer_status: str

class StudyPlanOutput(BaseModel):
    learner_id: str
    certification: str
    total_recommended_hours: float
    adjusted_daily_allocation: float
    reasoning_metadata: ReasoningMetadataSchema
    milestones: List[MilestoneSchema]
    iq_layer_applied: str

class EngagementOutput(BaseModel):
    employee_id: str
    action: str
    context_grounding_source: str
    iq_layer_applied: str

class AssessmentOutput(BaseModel):
    target_eval_learner: str
    required_passing_threshold: str
    historical_baseline_score_avg: float
    status: str
    iq_layer_applied: str

class ManagerInsightsOutput(BaseModel):
    aggregate_risk_metric: str
    foundry_source_insight: str
    compliance_safety_check: str
    iq_layer_applied: str
