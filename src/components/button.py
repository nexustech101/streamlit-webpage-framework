# button.py
import streamlit as st
from typing import Callable, Any, Optional

class Button:
    """
    Streamlit button component with advanced configuration options.
    """
    
    def __init__(
        self, 
        text: str, 
        action: Optional[Callable] = None,
        key: Optional[str] = None,
        help: Optional[str] = None,
        use_container_width: bool = False
    ) -> None:
        """
        Initialize a Streamlit button.
        
        Args:
            text (str): Button display text.
            action (Optional[Callable]): Function to call when button is clicked.
            key (Optional[str]): Unique key for the button.
            help (Optional[str]): Tooltip text for the button.
            use_container_width (bool): Whether to expand button to container width.
        """
        self.text = text
        self.action = action
        self.key = key
        self.help = help
        self.use_container_width = use_container_width
    
    def render(self) -> Any:
        """
        Render the button in Streamlit.
        
        Returns:
            Any: Result of button click or button rendering.
        """
        button_kwargs = {
            'label': self.text,
            'key': self.key,
            'help': self.help,
            'use_container_width': self.use_container_width
        }
        
        # Remove None values
        button_kwargs = {k: v for k, v in button_kwargs.items() if v is not None}
        
        if self.action:
            return st.button(**button_kwargs, on_click=self.action)
        return st.button(**button_kwargs)

