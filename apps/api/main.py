from collections.abc import AsyncIterable
from email import message
from fastapi.sse import EventSourceResponse, ServerSentEvent
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from sse_starlette import ServerSentEvent

from src.graph.state import state
from src.graph.bootstrap import Bootstrap
from src.runtime.orchestrator import Orchestrator, Workflow, Workflow

app = FastAPI(title="Agentic Mentorship Platform")

import time


async def data_streamer(agent_response):
    print("stream started")    
    for chunk in agent_response:
        print("Chunk type:", chunk.content)
        # print("repr:::", repr(chunk))
        yield f"data: {chunk.content}\n\n"

@app.get("/health")
async def health():
    return {"status": "healthy"}

class UserQuery(BaseModel):
    user_query: str
    


@app.post("/chat/stream", response_class=EventSourceResponse)
async def stream_agent_response(user_query: UserQuery) -> AsyncIterable[str]:
    start = time.time()

    bootstrap = Bootstrap()
    bootstrap.register_agents()
    bootstrap.register_llms()

    state["user_query"] = user_query.user_query
    
    print("Received user query: ", state)

    orchastrator = Orchestrator()
    
    orchastrator.run(Workflow.TUTOR, "state")
    
    print("workflow finished", time.time() - start)
    
    formatted_text = ''
     
    print("stream started")    
    for chunk in state["agent_response"]:
        print(chunk)
        
        yield chunk.content
        # yield ServerSentEvent(data=str(chunk.content), event="Token", id=str(1 + 1), retry=5000)

# @app.post("/chat/stream", response_class=StreamingResponse)
# async def stream_agent_response(user_query: UserQuery) -> AsyncIterable[str]:
#     start = time.time()

#     bootstrap = Bootstrap()
#     bootstrap.register_agents()
#     bootstrap.register_llms()

#     state["user_query"] = user_query.user_query
    
#     print("Received user query: ", state)

#     orchastrator = Orchestrator()
    
#     orchastrator.run(Workflow.TUTOR, "state")
    
#     print("workflow finished", time.time() - start)
        
#     return StreamingResponse(
#         data_streamer(state["agent_response"]), 
#         media_type='text/event-stream'
#     )        

@app.post("/agent/invoke", response_class=StreamingResponse)
async def invoke_agent(user_query: UserQuery) -> AsyncIterable[str]:

    # for line in user_query.user_query.splitlines():
    #     yield line
    bootstrap = Bootstrap()
    bootstrap.register_agents()
    bootstrap.register_llms()
    
    state["user_query"] = user_query.user_query

    orchastrator = Orchestrator()
    
    orchastrator.run(Workflow.TUTOR, state)
    
    yield state["agent_response"]
