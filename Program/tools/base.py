from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseTool(ABC):
    """
    Base class for all BlueFox tools.
    Ensures a consistent interface: input -> logic -> structured output.
    """

    @property
    @abstractmethod
    def category(self) -> str:
        """The category this tool belongs to (e.g., 'NETWORK', 'OSINT')."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """The human-readable name of the tool."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """A short description of what the tool does."""
        pass

    @property
    def required_inputs(self) -> Dict[str, str]:
        """
        Returns a dictionary of {input_name: prompt_text}.
        Override this to specify what inputs the tool needs.
        """
        return {}

    @abstractmethod
    def run(self, **kwargs) -> Dict[str, Any]:
        """
        The core logic of the tool.
        Must return a dictionary of results.
        Must NOT contain any print() or input() calls.
        """
        pass
