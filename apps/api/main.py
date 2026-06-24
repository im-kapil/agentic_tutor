from collections.abc import AsyncIterable
from email import message
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from src.graph.state import state
from src.graph.bootstrap import Bootstrap
from src.runtime.orchestrator import Orchestrator, Workflow, Workflow

app = FastAPI(title="Agentic Mentorship Platform")

@app.get("/health")
async def health():
    return {"status": "healthy"}

message = """
Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
Morty: (rubs his eyes) What, Rick? What's going on?
Rick: I got a surprise for you, Morty.
Morty: It's the middle of the night. What are you talking about?
Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
Morty: Ow! Ow! You're tugging me too hard!
Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
"""

class UserQuery(BaseModel):
    user_query: str

@app.post("/agent/stream", response_class=StreamingResponse)
async def invoke_agent(user_query: UserQuery) -> AsyncIterable[str]:

    for line in message.splitlines():
        yield line


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
