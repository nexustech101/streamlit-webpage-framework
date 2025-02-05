import streamlit as st
from typing import Any, Optional
from .base import BaseComponent

class Text(BaseComponent):
    """
    Streamlit text component with enhanced text manipulation capabilities.
    """
    
    def render(self, style: Optional[dict] = None) -> Any:
        """
        Render the text component in Streamlit.
        
        Args:
            style (Optional[dict]): Optional styling to be applied.
        
        Returns:
            Any: Streamlit text rendering result.
        """
        # If style is provided, use markdown for more flexible styling
        if style:
            # Convert style dict to CSS-like inline styling
            style_str = '; '.join(f"{k}: {v}" for k, v in style.items())
            styled_text = f'<span style="{style_str}">{self._content}</span>'
            return st.markdown(styled_text, unsafe_allow_html=True)
        
        # Default rendering
        return st.text(self._content)
    
    def upper(self) -> str:
        """
        Convert text to uppercase.
        
        Returns:
            str: Uppercase version of the text.
        """
        return self._content.upper()

    def lower(self) -> str:
        """
        Convert text to lowercase.
        
        Returns:
            str: Lowercase version of the text.
        """
        return self._content.lower()

    def capitalize(self) -> str:
        """
        Capitalize the first letter of the text.
        
        Returns:
            str: Capitalized text.
        """
        return self._content.capitalize()

    def allcaps(self) -> str:
        """
        Capitalize each word in the text.
        
        Returns:
            str: Text with each word capitalized.
        """
        return ' '.join(word.capitalize() for word in self._content.split())