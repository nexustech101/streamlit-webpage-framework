import streamlit as st
from typing import Any, Optional, List, Union, Callable
from .base import BaseComponent

class Layout(BaseComponent):
    """
    Advanced layout management component for Streamlit applications.
    Provides flexible column, row, and container-based layouts.
    """
    
    def __init__(self, key: Optional[str] = None):
        """
        Initialize the Layout component.
        
        Args:
            key (Optional[str]): Unique key for the layout
        """
        super().__init__(None, key)
        self._columns = []
        self._rows = []
    
    def columns(
        self, 
        spec: Union[int, List[int]], 
        gap: str = "small"
    ) -> 'Layout':
        """
        Create columns with flexible width specifications.
        
        Args:
            spec (Union[int, List[int]]): 
                - If int: number of equal-width columns
                - If List[int]: specific column width ratios
            gap (str): Space between columns ('small', 'medium', 'large')
        
        Returns:
            Layout instance for method chaining
        """
        if isinstance(spec, int):
            # Equal-width columns
            self._columns = st.columns(spec, gap=gap)
        elif isinstance(spec, list):
            # Custom-width columns
            self._columns = st.columns(spec, gap=gap)
        
        return self
    
    def with_columns(
        self, 
        content: List[Union[Callable, Any]]
    ) -> 'Layout':
        """
        Populate columns with content.
        
        Args:
            content (List[Union[Callable, Any]]): 
            List of components or render functions for each column
        
        Returns:
            Layout instance
        """
        if len(content) > len(self._columns):
            raise ValueError("More content than columns")
        
        for col, item in zip(self._columns, content):
            with col:
                if callable(item):
                    item()
                elif hasattr(item, 'render'):
                    item.render()
                else:
                    st.write(item)
        
        return self
    
    def expander(
        self, 
        label: str, 
        expanded: bool = False
    ) -> Any:
        """
        Create an expandable section.
        
        Args:
            label (str): Expander section label
            expanded (bool): Whether section is initially expanded
        
        Returns:
            Streamlit expander context
        """
        return st.expander(label, expanded=expanded)
    
    def container(self) -> Any:
        """
        Create a container for grouped components.
        
        Returns:
            Streamlit container context
        """
        return st.container()
    
    def divider(self) -> 'Layout':
        """
        Add a horizontal divider.
        
        Returns:
            Layout instance
        """
        st.divider()
        return self
    
    def spacer(self, height: int = 1) -> 'Layout':
        """
        Add vertical space.
        
        Args:
            height (int): Number of vertical spaces to add
        
        Returns:
            Layout instance
        """
        for _ in range(height):
            st.write("")
        return self
    
    def render(self) -> 'Layout':
        """
        Placeholder render method to maintain BaseComponent interface.
        
        Returns:
            Layout instance
        """
        return self