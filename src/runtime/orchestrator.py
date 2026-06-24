from enum import Enum

from src.workflows.tutor_workflow import TutorWorkflow

class Workflow(Enum):
    TUTOR = TutorWorkflow
    ABC = "ABC"

class Orchestrator:

    def run(self, workflow, state):
        match workflow:
            case Workflow.TUTOR:
                workflow = Workflow.TUTOR.value()
                
                print(f"Starting workflow: {workflow}")
                
                workflow.start()
                            
                return state
            case _:
                print(f"Workflow {workflow} not found")     
