import streamlit as st
from PIL import Image
import numpy as np

def main():
    # Configuration
    st.set_page_config(
        page_title="Durian Counter AI",
        page_icon="🍈", page_icon="",
        layout="wide"
    )

    # Header Section
    st.title("🍈 DurianCount AI")
    st.subheader("Automated Durian Detection & Counting System")
    
    #menambahkan file ini
    
    #perubahan kedua
    
    #perubahan ketiga
    
    #perubahan empat
    
    #ssdf

    # Project Description
    st.markdown("---")
    st.header("About the Project")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        DurianCount AI is an advanced mobile application that leverages YOLOv11 
        architecture for precise durian fruit detection and counting on trees. 
        
        Key Features:
        - Real-time durian detection
        - Accurate fruit counting
        - Mobile-optimized performance
        - Support for various durian varieties
        - Yield estimation capabilities
        """)
    
    with col2:
        # Placeholder for demo image
        st.image("https://placeholder.com/400x300", 
                caption="Durian Detection Demo",
                use_column_width=True)

    # Technical Specifications
    st.markdown("---")
    st.header("Technical Overview")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.subheader("Model Architecture")
        st.write("""
        - Base Model: YOLOv11
        - Input Resolution: 640x640
        - Optimization: TensorRT
        - Platform: Android Native
        """)
        
    with tech_col2:
        st.subheader("Performance Metrics")
        st.write("""
        - Average Precision (AP): 91.5%
        - Inference Time: 150ms
        - Minimum Android Version: 8.0
        - Model Size: 15MB
        """)

    # Demo Section
    st.markdown("---")
    st.header("Try Demo")
    
    uploaded_file = st.file_uploader("Upload an image of durian tree", 
                                   type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Process Image'):
            st.info('Processing... (Demo Mode)')
            st.write("Detected Durians: 12 (Sample Output)")

    # Application Process Flow
    st.markdown("---")
    st.header("How It Works")
    
    process_steps = {
        "1. Image Capture": "Use your Android device to photograph durian trees",
        "2. AI Processing": "YOLOv11 model analyzes the image in real-time",
        "3. Detection": "Advanced algorithms identify individual durians",
        "4. Counting": "Automated counting with position tracking",
        "5. Results": "Display count and generate yield estimates"
    }
    
    for step, description in process_steps.items():
        st.write(f"**{step}**: {description}")

    # Contact Section
    st.markdown("---")
    st.header("Contact Development Team")
    
    contact_form = st.form("contact_form")
    with contact_form:
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

    if submit:
        st.success("Thank you for your interest! We'll respond shortly.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>© 2024 DurianCount AI | Powered by YOLOv11</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
import streamlit as st
from PIL import Image
import numpy as np

def main():
    # Configuration
    st.set_page_config(
        page_title="Durian Counter AI",
        page_icon="🍈",
        layout="wide"
    )

    # Header Section
    st.title("🍈 DurianCount AI")
    st.subheader("Automated Durian Detection & Counting System")

    # Project Description
    st.markdown("---")
    st.header("About the Project")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        DurianCount AI is an advanced mobile application that leverages YOLOv11 
        architecture for precise durian fruit detection and counting on trees. 
        
        Key Features:
        - Real-time durian detection
        - Accurate fruit counting
        - Mobile-optimized performance
        - Support for various durian varieties
        - Yield estimation capabilities
        """)
    
    with col2:
        # Placeholder for demo image
        st.image("https://placeholder.com/400x300", 
                caption="Durian Detection Demo",
                use_column_width=True)

    # Technical Specifications
    st.markdown("---")
    st.header("Technical Overview")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.subheader("Model Architecture")
        st.write("""
        - Base Model: YOLOv11
        - Input Resolution: 640x640
        - Optimization: TensorRT
        - Platform: Android Native
        """)
        
    with tech_col2:
        st.subheader("Performance Metrics")
        st.write("""
        - Average Precision (AP): 91.5%
        - Inference Time: 150ms
        - Minimum Android Version: 8.0
        - Model Size: 15MB
        """)

    # Demo Section
    st.markdown("---")
    st.header("Try Demo")
    
    uploaded_file = st.file_uploader("Upload an image of durian tree", 
                                   type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Process Image'):
            st.info('Processing... (Demo Mode)')
            st.write("Detected Durians: 12 (Sample Output)")

    # Application Process Flow
    st.markdown("---")
    st.header("How It Works")
    
    process_steps = {
        "1. Image Capture": "Use your Android device to photograph durian trees",
        "2. AI Processing": "YOLOv11 model analyzes the image in real-time",
        "3. Detection": "Advanced algorithms identify individual durians",
        "4. Counting": "Automated counting with position tracking",
        "5. Results": "Display count and generate yield estimates"
    }
    
    for step, description in process_steps.items():
        st.write(f"**{step}**: {description}")

    # Contact Section
    st.markdown("---")
    st.header("Contact Development Team")
    
    contact_form = st.form("contact_form")
    with contact_form:
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

    if submit:
        st.success("Thank you for your interest! We'll respond shortly.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>© 2024 DurianCount AI | Powered by YOLOv11</p>
    </div>
    """, unsafe_allow_html=True)
    
    #sdfdsdfsdf

if __name__ == "__main__":
    main()
