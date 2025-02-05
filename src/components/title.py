import streamlit as st
from typing import Any, Optional, Callable
from .base import BaseComponent


class Title(BaseComponent):
    """
    Streamlit title component with text transformation capabilities.
    """

    def render(self, style: Optional[dict] = None) -> Any:
        """
        Render the title component in Streamlit.
        
        Args:
            style (Optional[dict]): Optional styling dictionary for the title.
        
        Returns:
            Any: Streamlit title rendering result.
        """
        if style:
            # Apply custom styling if provided
            return st.title(self._text, **style)
        return st.title(self._text)

    def subheader(self, style: Optional[dict] = None) -> Any:
        """
        Render as a Streamlit subheader.
        
        Args:
            style (Optional[dict]): Optional styling dictionary for the subheader.
        
        Returns:
            Any: Streamlit subheader rendering result.
        """
        if style:
            return st.subheader(self._text, **style)
        return st.subheader(self._text)
