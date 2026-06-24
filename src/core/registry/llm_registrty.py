"""
Central Registry
================
Single source of truth for every LLM.

Usage
-----
    # Registration (done once, usually in __init__.py)
    registry.register_llm("gpt-4", GPT4LLM)

    # Resolution (anywhere in the app)
    llm_cls = registry.get_llm("gpt-4")
    llm     = llm_cls(llm_info)
"""

from __future__ import annotations

import threading
from typing import TYPE_CHECKING, Type, TypeVar, Dict

import structlog

from src.llms.base_llm import base_model

if TYPE_CHECKING:
    from src.core.base_llm import BaseLLM

log = structlog.get_logger(__name__)

T = TypeVar("T")

class LLMRegistry:
    """Thread-safe registry backed by plain dicts."""

    _lock = threading.Lock()

    _registry: Dict[str, Type[BaseLLM]] = {}

    def __init__(self) -> None:
        self._llms:    dict[str, type[BaseLLM]]    = {}

    # ── Generic helpers ───────────────────────────────────────────────────────
    
    @classmethod
    def register(cls, name: str, llm_cls: Type[BaseLLM]):
        cls._registry[name] = llm_cls
        
    @classmethod
    def get(cls, name: str):
        if name not in cls._registry:
            raise ValueError(f"LLM '{name}' not registered")
        return cls._registry[name]
    
    @classmethod
    def list(cls):
        return list(cls._registry.keys())

    def llm(self, name: str):
        def decorator(cls: type[BaseLLM]) -> type[BaseLLM]:
            self.register_llm(name, cls)
            return cls
        return decorator
    
    @classmethod
    def snapshot(self) -> dict[str, list[str]]:
        """Return a dict snapshot of all registered entries — useful for /health."""
        return {
            "agents": self.list_agents(),
            "llms":   self.list_llms(),
        }