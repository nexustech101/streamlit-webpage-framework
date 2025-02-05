# Streamlit Component Framework

A modular and extensible framework for building structured Streamlit applications with reusable components. This framework provides a collection of base components and utilities that make it easier to create consistent, maintainable Streamlit web applications.

## Features

- 🎨 **Modular Component System**: Base components for common UI elements
- 📏 **Flexible Layouts**: Advanced layout management with columns and containers
- 🧭 **Navigation**: Built-in sidebar navigation system
- 🎯 **Type Safety**: Full typing support with Python type hints
- 🔧 **Extensible**: Easy to create custom components
- 🎨 **Styling**: Flexible styling options for all components

## Installation

```bash
pip install streamlit
# Additional installation steps for your package
```

## Project Structure

```
.
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── button.py
│   │   ├── container.py
│   │   ├── data_display.py
│   │   ├── header.py
│   │   ├── image.py
│   │   ├── layout.py
│   │   ├── navigation.py
│   │   ├── text.py
│   │   └── title.py
│   └── global/
├── static/
└── test/
    └── test.py
```

### Directory Structure Overview

- **src/**: Main source code directory
  - **app.py**: Main application entry point
  - **components/**: Reusable UI components
  - **global/**: Global configurations and utilities
- **static/**: Static assets (images, CSS, etc.)
- **test/**: Test files and test utilities

## Core Components

### BaseComponent

The foundation of the component system. All components inherit from this abstract base class, ensuring a consistent interface.

```python
from src.components.base import BaseComponent

class CustomComponent(BaseComponent):
    def render(self):
        # Implement render logic here
        pass
```

### Layout

Manages the page structure with flexible column and container layouts.

```python
from src.components import Layout

layout = Layout()
layout.columns([1, 2, 1])  # Create three columns with ratio 1:2:1
layout.with_columns([
    lambda: component1.render(),
    lambda: component2.render(),
    lambda: component3.render()
])
```

### Container

Groups related components together with various layout options.

```python
from src.components import Container

container = Container()
container.add(component1)
container.add(component2)
container.render(layout='vertical')  # or 'horizontal', 'columns'
```

### Button

Creates interactive buttons with customizable actions.

```python
from src.components import Button

button = Button(
    text="Click Me",
    action=lambda: print("Clicked!"),
    key="unique_key"
)
button.render()
```

### Navigation

Implements sidebar navigation with configurable sections.

```python
from src.components import Sidebar

sidebar = Sidebar()
sidebar.add_section("Home", action=lambda: show_home())
sidebar.add_section("About", action=lambda: show_about())
sidebar.render()
```

## Example Application

```python
from src.components import Layout, Container, Text, Header, Button

def main():
    layout = Layout()
    
    # Create header section
    header = Header("Welcome")
    header.render(level=1)
    
    # Create two-column layout
    layout.columns(2)
    layout.with_columns([
        lambda: Text("Left column content").render(),
        lambda: Text("Right column content").render()
    ])
    
    # Add action button
    button = Button("Click Me", action=lambda: print("Clicked!"))
    button.render()

if __name__ == "__main__":
    main()
```

## Component Properties

### Common Properties

Most components support these common properties:

- `key`: Unique identifier for the component
- `style`: Dictionary of CSS styles
- `render()`: Method to display the component

### Specific Component Properties

#### Layout
- `columns(spec)`: Create column layout with specified ratios
- `with_columns(content)`: Add content to columns
- `divider()`: Add horizontal divider
- `spacer(height)`: Add vertical space

#### Button
- `text`: Button label
- `action`: Callback function
- `use_container_width`: Expand to container width

#### Header/Text
- `level`: Header level (1-6)
- `upper()`: Convert to uppercase
- `lower()`: Convert to lowercase
- `capitalize()`: Capitalize first letter

## Styling

Components support custom styling through style dictionaries:

```python
header = Header("Title")
header.render(style={
    "color": "blue",
    "font-size": "24px",
    "font-weight": "bold"
})
```

## Best Practices

1. **Project Organization**
   - Keep source code in the `src` directory
   - Store static assets in the `static` directory
   - Maintain tests in the `test` directory
   - Use the `global` directory for project-wide configurations

2. **Component Organization**
   - Keep related components grouped together
   - Use containers for logical grouping
   - Maintain consistent styling across components

3. **Layout Management**
   - Plan your layout structure before implementation
   - Use appropriate column ratios for responsive design
   - Consider mobile viewports when designing layouts

4. **Performance**
   - Avoid unnecessary re-renders
   - Use keys consistently
   - Cache expensive computations

5. **Type Safety**
   - Use type hints for all component properties
   - Validate input data before rendering
   - Handle edge cases and errors gracefully

## Testing

Test files are located in the `test` directory. To run tests:

```bash
python -m pytest test/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Your License Here]

## Author

Charles L. Defreese III

## Version

1.0.0