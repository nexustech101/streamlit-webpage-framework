import streamlit as st
from typing import Union, Optional, Any
from .base import BaseComponent

class ImageDisplay(BaseComponent):
    """
    Advanced image display component with multiple rendering options.
    """
    
    def __init__(
        self, 
        image: Union[str, bytes], 
        key: Optional[str] = None
    ):
        """
        Initialize image display.
        
        Args:
            image (Union[str, bytes]): Image source (path or bytes)
            key (Optional[str]): Unique key
        """
        super().__init__(image, key)
    
    def render(
        self, 
        caption: Optional[str] = None, 
        width: Optional[int] = None,
        use_column_width: bool = False
    ) -> Any:
        """
        Render image with flexible configuration.
        
        Args:
            caption (Optional[str]): Image caption
            width (Optional[int]): Image width
            use_column_width (bool): Expand to column width
        
        Returns:
            Streamlit image component
        """
        return st.image(
            self._content, 
            caption=caption, 
            width=width, 
            use_column_width=use_column_width
        )