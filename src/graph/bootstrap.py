import os
import dotenv
dotenv.load_dotenv()

from src.agents.tutor_agent.tutor_agent import TutorAgent
from src.core.registry.agent_registry import AgentRegistry
from src.core.registry.llm_registrty import LLMRegistry
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_ollama import ChatOllama

class Bootstrap:
    def __init__(self):
        # agents = self.register_agents()
        # llms = self.register_llms()
        pass
    # ____________TODO: All these registry to be moved at app container level and not in bootstrap.____________

    # Register agents
    def register_agents(self):
        AgentRegistry._register("tutor_agent", TutorAgent) 
    
    
    # Register LLMs
    def register_llms(self):
        LLMRegistry.register("openai/gpt-oss-120b",
            ChatNVIDIA(
                model="openai/gpt-oss-120b",
                api_key=os.getenv("NVIDIA_MODEL_API_KEY"),
                temperature=0,
                max_tokens=4096
            )
        )

        LLMRegistry.register("qwen2.5", 
        ChatOllama(
            model="qwen2.5",
            validate_model_on_init=True,
            temperature=0,
            ).bind_tools([])
        )
        
    #TODO: Define tool registry and add tools here
    #TODO: Define workflow registry and add workflows here
    #TODO: Define knowledge graph registry and add knowledge graphs here