import streamlit as st
from components import (
    Layout, 
    Container, 
    Text, 
    Header, 
    Button, 
    Sidebar, 
    ImageDisplay
)

def main():
    # Create layout
    layout = Layout()
    
    # Sidebar Navigation
    sidebar = Sidebar()
    sidebar.add_section("Home")
    sidebar.add_section("Features")
    sidebar.add_section("Pricing")
    sidebar.render()
    
    # Hero Section
    layout.columns([1, 2, 1])
    layout.with_columns([
        lambda: None,  # Empty left column
        lambda: _render_hero_section(),
        lambda: None   # Empty right column
    ])
    
    # Features Section
    layout.divider()
    _render_features_section(layout)
    
    # Pricing Section
    layout.divider()
    _render_pricing_section(layout)

def _render_hero_section():
    """
    Render the hero section of the landing page.
    """
    # Container for hero content
    hero_container = Container()
    
    # Header
    hero_header = Header("Revolutionize Your Workflow")
    hero_header.render(level=1)
    
    # Subheader
    Text("Streamline your projects with cutting-edge components").render()
    
    # Call to Action Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        start_button = Button(
            text="Get Started", 
            action=lambda: st.success("Welcome aboard!")
        )
        start_button.render()
    
    with col2:
        demo_button = Button(
            text="View Demo", 
            action=lambda: st.info("Launching demo...")
        )
        demo_button.render()

def _render_features_section(layout):
    """
    Render the features section with a grid layout.
    """
    # Features Header
    Header("Why Choose Our Solution").render(level=2)
    Text("Powerful features designed to supercharge your productivity").render()
    
    # Create 3 columns for features
    layout.columns(3)
    layout.with_columns([
        lambda: _feature_card(
            "🚀 Lightning Fast", 
            "Optimized components for maximum performance"
        ),
        lambda: _feature_card(
            "🔧 Highly Customizable", 
            "Flexible design that adapts to your unique needs"
        ),
        lambda: _feature_card(
            "📊 Data-Driven", 
            "Seamless integration with your data workflows"
        )
    ])

def _feature_card(title: str, description: str):
    """
    Create a feature card with title and description.
    """
    st.markdown(f"""
    <div style="
        border: 1px solid #e1e4e8;
        border-radius: 6px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    " onmouseover="this.style.transform='scale(1.05)'"
    onmouseout="this.style.transform='scale(1)'">
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

def _render_pricing_section(layout):
    """
    Render the pricing section with different tiers.
    """
    # Pricing Header
    Header("Simple, Transparent Pricing").render(level=2)
    Text("Choose the plan that fits your needs").render()
    
    # Create 3 columns for pricing tiers
    layout.columns(3)
    layout.with_columns([
        lambda: _pricing_card(
            "Starter", 
            "$0", 
            ["Basic Components", "Community Support", "Limited Access"]
        ),
        lambda: _pricing_card(
            "Pro", 
            "$29", 
            ["Advanced Components", "Priority Support", "Regular Updates"]
        ),
        lambda: _pricing_card(
            "Enterprise", 
            "Custom", 
            ["Full Access", "Dedicated Support", "Custom Solutions"]
        )
    ])

def _pricing_card(title: str, price: str, features: list):
    """
    Create a pricing card with different tiers.
    """
    st.markdown(f"""
    <div style="
        border: 1px solid #e1e4e8;
        border-radius: 6px;
        padding: 20px;
        text-align: center;
        background-color: {'#f6f8fa' if title != 'Pro' else '#e1e4e8'};
    ">
        <h3>{title}</h3>
        <h1>{price} <small style="font-size: 0.5em;">{'/month' if price != 'Custom' else ''}</small></h1>
        <ul style="list-style-type: none; padding: 0;">
            {''.join(f'<li>✓ {feature}</li>' for feature in features)}
        </ul>
        <button style="
            background-color: {'#0366d6' if title == 'Pro' else '#2ea44f'};
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            cursor: pointer;
        ">Select {title}</button>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()