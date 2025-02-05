from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, Callable

class BaseComponent(ABC):
    """
    Abstract base class for all Streamlit components.
    Provides a consistent interface and common functionality.
    """
    
    def __init__(self, content: Any, key: Optional[str] = None):
        """
        Initialize the base component.
        
        Args:
            content (Any): The content to be displayed
            key (Optional[str]): Optional unique key for the component
        """
        self._content = content
        self._key = key or f"component_{id(self)}"
    
    @property
    def key(self) -> str:
        """Unique identifier for the component."""
        return self._key
    
    @abstractmethod
    def render(self, **kwargs) -> Any:
        """
        Abstract method to render the component.
        
        Raises:
            NotImplementedError if not implemented by subclass.
        """
        raise NotImplementedError("Subclasses must implement render method")