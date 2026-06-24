from langchain.agents import AgentState

state: AgentState = {
    
    "messages": [],
    "user_query": "",
    "agent_response": "",

    # workflow_name: str

    # execution_plan: list[str]

    # memory_context: str

    # retrieved_documents: list[dict[str, Any]]

    # metadata: dict[str, Any]

    # errors: list[str]
}