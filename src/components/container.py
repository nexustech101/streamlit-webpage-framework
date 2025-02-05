import streamlit as st
from typing import Any, Optional, List, Callable
from .base import BaseComponent

class Container(BaseComponent):
    """
    Advanced container component for Streamlit with flexible rendering options.
    """
    
    def __init__(
        self, 
        content: Optional[List[Any]] = None, 
        key: Optional[str] = None
    ):
        """
        Initialize a container with optional content.
        
        Args:
            content (Optional[List[Any]]): List of components or content to display
            key (Optional[str]): Unique key for the container
        """
        super().__init__(content, key)
        self._content = content or []
    
    def add(self, component: Any) -> None:
        """
        Add a component to the container.
        
        Args:
            component (Any): Component or content to add
        """
        self._content.append(component)
    
    def render(
        self, 
        layout: str = 'vertical', 
        columns: Optional[int] = None,
        style: Optional[dict] = None
    ) -> Any:
        """
        Render the container with various layout options.
        
        Args:
            layout (str): Rendering layout ('vertical', 'horizontal', 'columns')
            columns (Optional[int]): Number of columns for column layout
            style (Optional[dict]): Additional styling options
        
        Returns:
            Any: Rendered Streamlit components
        """
        # Vertical layout (default)
        if layout == 'vertical':
            for item in self._content:
                if hasattr(item, 'render'):
                    item.render()
                else:
                    st.write(item)
        
        # Horizontal layout
        elif layout == 'horizontal':
            cols = st.columns(len(self._content))
            for col, item in zip(cols, self._content):
                with col:
                    if hasattr(item, 'render'):
                        item.render()
                    else:
                        st.write(item)
        
        # Column layout
        elif layout == 'columns':
            if not columns:
                columns = len(self._content)
            
            cols = st.columns(columns)
            for i, item in enumerate(self._content):
                with cols[i % columns]:
                    if hasattr(item, 'render'):
                        item.render()
                    else:
                        st.write(item)
        
        return self