from ..src.components import \
(
    Button, 
    Container, 
    Header, 
    Text, 
    Layout, 
    Sidebar,
    ImageDisplay,
    JSONDisplay
)
import pytest
import streamlit as st


# Mock streamlit functions to avoid runtime errors
@pytest.fixture(autouse=True)
def mock_streamlit(monkeypatch):
    """Mock streamlit functions for testing"""
    def mock_button(*args, **kwargs):
        return True
    
    def mock_text(*args, **kwargs):
        return None
    
    def mock_header(*args, **kwargs):
        return None
    
    def mock_columns(*args, **kwargs):
        return [type('MockColumn', (), {'__enter__': lambda x: None, '__exit__': lambda x, *args: None})] * 3
    
    def mock_sidebar(*args, **kwargs):
        return type('MockSidebar', (), {'__enter__': lambda x: None, '__exit__': lambda x, *args: None})()
    
    def mock_image(*args, **kwargs):
        return None
    
    # Apply mocks
    monkeypatch.setattr(st, "button", mock_button)
    monkeypatch.setattr(st, "text", mock_text)
    monkeypatch.setattr(st, "header", mock_header)
    monkeypatch.setattr(st, "columns", mock_columns)
    monkeypatch.setattr(st, "sidebar", mock_sidebar)
    monkeypatch.setattr(st, "image", mock_image)

class TestButton:
    """Test suite for Button component"""
    
    def test_button_initialization(self):
        """Test button initialization with basic properties"""
        button = Button(text="Test Button")
        assert button.text == "Test Button"
        assert button.action is None
        assert button.use_container_width is False
    
    def test_button_with_action(self):
        """Test button with custom action"""
        action_called = False
        
        def test_action():
            nonlocal action_called
            action_called = True
        
        button = Button(text="Action Button", action=test_action)
        button.render()
        assert action_called is True

class TestContainer:
    """Test suite for Container component"""
    
    def test_container_initialization(self):
        """Test container initialization"""
        container = Container()
        assert container._content == []
    
    def test_container_add_component(self):
        """Test adding components to container"""
        container = Container()
        text = Text("Test Text")
        container.add(text)
        assert len(container._content) == 1
        assert container._content[0] == text
    
    def test_container_render_vertical(self):
        """Test vertical layout rendering"""
        container = Container()
        container.add(Text("Text 1"))
        container.add(Text("Text 2"))
        result = container.render(layout='vertical')
        assert result == container

class TestHeader:
    """Test suite for Header component"""
    
    def test_header_initialization(self):
        """Test header initialization"""
        header = Header("Test Header")
        assert header._content == "Test Header"
    
    def test_header_text_transformations(self):
        """Test header text transformation methods"""
        header = Header("test header")
        assert header.upper() == "TEST HEADER"
        assert header.lower() == "test header"
        assert header.capitalize() == "Test header"
        assert header.allcaps() == "Test Header"

class TestText:
    """Test suite for Text component"""
    
    def test_text_initialization(self):
        """Test text initialization"""
        text = Text("Test Text")
        assert text._content == "Test Text"
    
    def test_text_with_style(self):
        """Test text rendering with custom style"""
        text = Text("Styled Text")
        style = {"color": "red", "font-size": "20px"}
        text.render(style=style)

class TestLayout:
    """Test suite for Layout component"""
    
    def test_layout_initialization(self):
        """Test layout initialization"""
        layout = Layout()
        assert layout._columns == []
        assert layout._rows == []
    
    def test_layout_columns(self):
        """Test column creation"""
        layout = Layout()
        result = layout.columns(3)
        assert isinstance(result, Layout)
    
    def test_layout_with_columns(self):
        """Test adding content to columns"""
        layout = Layout()
        layout.columns(3)
        content = [
            lambda: Text("Col 1").render(),
            lambda: Text("Col 2").render(),
            lambda: Text("Col 3").render()
        ]
        result = layout.with_columns(content)
        assert isinstance(result, Layout)

class TestSidebar:
    """Test suite for Sidebar component"""
    
    def test_sidebar_initialization(self):
        """Test sidebar initialization"""
        sidebar = Sidebar()
        assert len(sidebar._items) == 0
    
    def test_add_section(self):
        """Test adding navigation sections"""
        sidebar = Sidebar()
        sidebar.add_section("Home")
        assert len(sidebar._items) == 1
        assert sidebar._items[0]["title"] == "Home"
    
    def test_section_with_action(self):
        """Test section with custom action"""
        action_called = False
        
        def test_action():
            nonlocal action_called
            action_called = True
            
        sidebar = Sidebar()
        sidebar.add_section("Home", action=test_action)
        sidebar.render()
        # Action should be called when section is rendered
        assert action_called is True

class TestJSONDisplay:
    """Test suite for JSONDisplay component"""
    
    def test_json_initialization(self):
        """Test JSON display initialization"""
        data = {"key": "value"}
        display = JSONDisplay(data)
        assert display._content == data
    
    def test_json_string_input(self):
        """Test JSON display with string input"""
        json_str = '{"key": "value"}'
        display = JSONDisplay(json_str)
        assert display._content == {"key": "value"}
    
    def test_invalid_json(self):
        """Test handling of invalid JSON"""
        invalid_json = "invalid json"
        display = JSONDisplay(invalid_json)
        assert display._content == {"error": "Invalid JSON"}

class TestImageDisplay:
    """Test suite for ImageDisplay component"""
    
    def test_image_initialization(self):
        """Test image display initialization"""
        image_path = "test_image.jpg"
        display = ImageDisplay(image_path)
        assert display._content == image_path
    
    def test_image_render_options(self):
        """Test image rendering with options"""
        display = ImageDisplay("test_image.jpg")
        display.render(
            caption="Test Caption",
            width=100,
            use_column_width=True
        )

def test_component_integration():
    """Test integration between multiple components"""
    # Create layout
    layout = Layout()
    layout.columns(2)
    
    # Create container
    container = Container()
    
    # Add components to container
    container.add(Header("Test Header"))
    container.add(Text("Test Text"))
    container.add(Button("Test Button"))
    
    # Render container in layout
    layout.with_columns([
        lambda: container.render(),
        lambda: Text("Second Column").render()
    ])
    
    # Assertions to verify integration
    assert True  # Add specific assertions based on expected behavior

if __name__ == "__main__":
    pytest.main([__file__])