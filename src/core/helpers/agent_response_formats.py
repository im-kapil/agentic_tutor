from dataclasses import dataclass, field
from typing import List, Dict, Literal, Optional

from pydantic import BaseModel

@dataclass
class TaskStep:
    step_id: int
    name: str
    description: str
    type: str
    target_files: List[str]
    dependencies: List[int]
    expected_output: Optional[str] = None

@dataclass
class PLANNER_AGENT_RESPONSE_FORMAT(BaseModel):
    project_name: str
    project_description: str
    project_type: str
    plan_id: str
    total_steps: list[int]
    
    steps: List[TaskStep] = field(default_factory=list)
    folder_structure: Dict[str, str] = field(default_factory=dict)

@dataclass
class SUPERVISOR_AGENT_RESPONSE_FORMAT(BaseModel):
    intent: Literal[
        "GENERAL_QUERY", 
        "TASK_EXECUTION", 
        "CODE_REVIEW", 
        "DEBUGGING", 
        "OPTIMIZATION",
        "CODING_HELP", 
        "PROJECT_SETUP",
        "BUG_FIXING",
        "DOC_GENERATE", 
        "DOC_READ", 
        "TECHNICAL"
    ]
    confidence: float
     
@dataclass
class TUTOR_AGENT_RESPONSE_FORMAT(BaseModel):
    agent_response: str
    
