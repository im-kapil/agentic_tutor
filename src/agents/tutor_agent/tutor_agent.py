from langchain.messages import HumanMessage, SystemMessage

from src.core.base_agent import BaseAgent
from src.core.helpers.agent_response_formats import TUTOR_AGENT_RESPONSE_FORMAT
from src.core.prompts.tutor_agent_system_prompt import TUTOR_AGENT_SYSTEM_PROMPT

class TutorAgent(BaseAgent):
    def execute(self, state):
        print(f"[{self.name}] Executing TutorAgent with state: ", state)
        
        # llm = self.llm.bind_tools(self.tools)
        llm_with_structured_output = self.llm.with_structured_output(TUTOR_AGENT_RESPONSE_FORMAT)
        
        messages =  [
                SystemMessage(content=TUTOR_AGENT_SYSTEM_PROMPT),
                HumanMessage(content=state["user_query"])
            ]
                
        llm_response = llm_with_structured_output.invoke(messages)
        
        state["agent_response"] = llm_response.model_dump_json()
        # print(f"[{self.name}] LLM Response: ", llm_response.model_dump_json())
        
        return state
