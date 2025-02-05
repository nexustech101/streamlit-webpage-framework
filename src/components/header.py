import streamlit as st
from typing import Any, Optional
from .base import BaseComponent

class Header(BaseComponent):
    """
    Streamlit header component with text transformation capabilities.
    """
    
    def __init__(
        self, 
        text: str, 
        key: Optional[str] = None
    ):
        """
        Initialize the Header component.
        
        Args:
            text (str): Header text
            key (Optional[str]): Unique key for the component
        """
        super().__init__(text, key)
    
    def render(self, level: int = 1, style: Optional[dict] = None) -> Any:
        """
        Render the header component in Streamlit.
        
        Args:
            level (int): Header level (1-6). Defaults to 1.
            style (Optional[dict]): Optional styling for the header
        
        Returns:
            Streamlit header rendering result
        """
        # Select appropriate rendering method based on header level
        render_method = getattr(st, f'header{level}' if level > 1 else 'header')
        
        # If style is provided, use markdown for more flexible styling
        if style:
            style_str = '; '.join(f"{k}: {v}" for k, v in style.items())
            styled_text = f'<span style="{style_str}">{self._content}</span>'
            return render_method(styled_text, unsafe_allow_html=True)
        
        # Default rendering
        return render_method(self._content)
    
    def upper(self) -> str:
        """
        Convert text to uppercase.
        
        Returns:
            str: Uppercase version of the text
        """
        return self._content.upper()
    
    def lower(self) -> str:
        """
        Convert text to lowercase.
        
        Returns:
            str: Lowercase version of the text
        """
        return self._content.lower()
    
    def capitalize(self) -> str:
        """
        Capitalize the first letter of the text.
        
        Returns:
            str: Capitalized text
        """
        return self._content.capitalize()
    
    def allcaps(self) -> str:
        """
        Capitalize each word in the text.
        
        Returns:
            str: Text with each word capitalized
        """
        return ' '.join(word.capitalize() for word in self._content.split())