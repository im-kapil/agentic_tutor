from src.graph.state import state

from src.core.registry.agent_registry import AgentRegistry
from src.core.registry.llm_registrty import LLMRegistry



class TutorWorkflow:
    def __init__(self):
        self.state = "initialized"
    
    def start(self):
        try:            
            # Get tutor agent from the registry
            tutor_agent = AgentRegistry.get_node(
            "tutor_agent",
            {
                "tools": [],
                "llm": LLMRegistry.get("qwen2.5")
            }
        )
            # Start the tutor agent's workflow  
            tutor_agent.execute(state)  # Assuming the agent has an execute method to start its process
            
        except Exception as e:
            self.state = "error"
            print(f"Error starting tutor workflow: {e}")    