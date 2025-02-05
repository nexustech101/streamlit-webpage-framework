import streamlit as st
from typing import List, Dict, Any, Callable, Optional
from .base import BaseComponent


class Sidebar(BaseComponent):
    """
    Advanced sidebar navigation and configuration component.
    """

    def __init__(self, key: str = 'sidebar'):
        """Initialize sidebar."""
        super().__init__(None, key)
        self._items: List[Dict[str, Any]] = []

    def add_section(
        self,
        title: str,
        action: Optional[Callable] = None
    ) -> 'Sidebar':
        """
        Add a navigation section to sidebar.
        
        Args:
            title (str): Section title
            action (Optional[Callable]): Action to trigger on selection
        
        Returns:
            Sidebar instance
        """
        self._items.append({
            'title': title,
            'action': action
        })
        return self

    def render(self) -> Any:
        """
        Render sidebar with navigation items.
        
        Returns:
            Selected sidebar item
        """
        with st.sidebar:
            for item in self._items:
                if st.button(item['title'], key=item['title']):
                    if item['action']:
                        item['action']()
        return self
