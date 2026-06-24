from src.graph.state import AgentState
from src.graph.bootstrap import Bootstrap
from src.runtime.orchestrator import Orchestrator, Workflow
from src.workflows.tutor_workflow import TutorWorkflow

def main():
    
    bootstrap = Bootstrap()
    bootstrap.register_agents()
    bootstrap.register_llms()
    
    orchastrator = Orchestrator()
    
    orchastrator.run(Workflow.TUTOR, AgentState)

if __name__ == "__main__":
    main()
