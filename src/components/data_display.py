import streamlit as st
import json
from typing import Any, Dict, Union
from .base import BaseComponent

class JSONDisplay(BaseComponent):
    """
    Component for displaying JSON data with syntax highlighting.
    """
    
    def __init__(
        self, 
        data: Union[Dict, str], 
        key: str = None,
        expanded: bool = False
    ):
        """
        Initialize JSON display.
        
        Args:
            data (Union[Dict, str]): JSON data to display
            key (Optional[str]): Unique key
            expanded (bool): Whether to expand the JSON view
        """
        # Convert string to dict if needed
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                data = {"error": "Invalid JSON"}
        
        super().__init__(data, key)
        self._expanded = expanded
    
    def render(
        self, 
        theme: str = 'default', 
        language: str = 'json'
    ) -> Any:
        """
        Render JSON with syntax highlighting.
        
        Args:
            theme (str): Syntax highlighting theme
            language (str): Code language
        
        Returns:
            Streamlit code block
        """
        return st.code(
            json.dumps(self._content, indent=2), 
            language=language
        )