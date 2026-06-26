from collections.abc import AsyncIterable
from fastapi.sse import EventSourceResponse, ServerSentEvent

from fastapi import FastAPI
from apps.api.common.requrest_payloads import UserQuery
from src.graph.state import state
from src.graph.bootstrap import Bootstrap
from src.runtime.orchestrator import Orchestrator, Workflow, Workflow

app = FastAPI(title="Agentic Mentorship Platform")

import time

@app.post("/chat/stream", response_class=EventSourceResponse)
async def stream_agent_response(user_query: UserQuery) -> AsyncIterable[str]:
    start = time.time()

    bootstrap = Bootstrap()
    bootstrap.register_agents()
    bootstrap.register_llms()

    state["user_query"] = user_query.user_query
    
    orchastrator = Orchestrator()
    
    orchastrator.run(Workflow.TUTOR, state)
    
    print("workflow finished", time.time() - start)
         
    print("stream started")    
    llm_full_response = ''
    for chunk in state["agent_response"]:
        print   (chunk)
        llm_full_response += chunk.content
        # yield chunk.content
        # yield ServerSentEvent(data=str(chunk.content), event="Token")
        yield ServerSentEvent(raw_data=chunk.content)
        

    
    #TODO: Implement event publishing here
    print(llm_full_response)
    yield llm_full_response

    