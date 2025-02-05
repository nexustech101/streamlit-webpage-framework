# Import key components or modules to make them easily accessible
from .components import *

# Optional: Define package-level metadata
__version__ = "1.0.0"
__author__ = "Charles L. Defreese III"

# Optional: You can create package-level configurations or constants
DEFAULT_CONFIG = {
    "app_name": "My Streamlit Application",
    "debug_mode": True
}

# Optional: Any package-level initialization logic
def init_app():
    """
    Initialize the application-level configurations or setup.
    This can be used for global settings, logging, etc.
    """
    # Example: Set up logging
    import logging
    logging.basicConfig(level=logging.INFO)
