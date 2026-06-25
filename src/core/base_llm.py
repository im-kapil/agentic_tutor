from abc import ABC, abstractmethod
import os
from typing import Dict, Any

import dotenv
dotenv.load_dotenv()


"""
BaseLLM
=========
Every LLM in the system inherits from this class.

Concrete LLMs must implement:
    • `build_graph()`  — return a compiled LangGraph CompiledGraph
    • `run()`          — execute a single user request end-to-end

The class stores an `llmInfo` descriptor (name, version, description, …)
so the registry and MCP server can introspect any agent uniformly.
"""
class BaseLLM(ABC):
    def __init__(
        self,
        name: str,
        llm,
        tools=None,
        skills=None,
    ):
        self.name = name
        self.llm = llm
        self.tools = tools or []
        self.skills = skills or []

    @abstractmethod
    def execute(self, state: Dict[str, Any]):
        pass