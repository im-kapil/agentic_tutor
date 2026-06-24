from src.graph.state import state
from src.graph.bootstrap import Bootstrap
from src.runtime.orchestrator import Orchestrator, Workflow
from src.workflows.tutor_workflow import TutorWorkflow

def main():
    
    bootstrap = Bootstrap()
    bootstrap.register_agents()
    bootstrap.register_llms()
    
    state["user_query"] = "How to make money online?"

    orchastrator = Orchestrator()
    
    orchastrator.run(Workflow.TUTOR, state)
    
    print("Final State: ", state)
    
if __name__ == "__main__":
    main()
