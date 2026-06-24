from __future__ import annotations
from typing import Any, TypedDict
from langchain_core.messages import BaseMessage
from src.core.helpers.agent_response_formats import PLANNER_AGENT_RESPONSE_FORMAT


class AgentState(TypedDict):
    """Shared mutable state threaded through every LangGraph node."""

    # Core I/O
    messages:       list[BaseMessage]   # full conversation / tool-call history
    user_query:    str                 # original user request (immutable)
    agent_response:   str                 # populated by the final node
    # plan:         PLANNER_AGENT_RESPONSE_FORMAT      # structured plan output from planner agent

    # # Execution tracking
    # iteration:      int                 # current iteration count
    # steps:          list[dict[str, Any]]  # structured trace of each step
    # errors:         list[str]           # accumulated error messages

    # # Context
    # workspace:      str                 # filesystem workspace path
    # metadata:       dict[str, Any]      # arbitrary agent-specific state
    # user_intent: str # distilled user intent to guide agent decision-making