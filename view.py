import streamlit as st
import working as wk
from PIL import Image
import os

def save_uploaded_file(uploaded_file):
    try:
        os.makedirs("uploads", exist_ok=True)
        img = Image.open(uploaded_file)
        img_path = os.path.join("uploads", uploaded_file.name)
        img.save(img_path, format='JPEG')
        return img_path
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def main():
    # Setting page title and icon
    st.set_page_config(page_title='Recipe Spoonly', page_icon='🍳', layout='wide')

    # Initialize session state
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    if 'cuisine' not in st.session_state:
        st.session_state.cuisine = None

    # Custom CSS for centering title and styling upload button
    st.markdown(
        """
        <style>
        .css-1l02zno {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .css-hi6a2p {
            width: 100px;
            margin-right: 20px;
        }
        .upload-btn {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
            background-color: #f63366;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .upload-btn:hover {
            background-color: #d10e3c;
        }
        .upload-btn:active {
            background-color: #b00a31;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .title {
            text-align: center;
            width: 100%;
        }
        .stButton button {
            background-color: #f63366;
            color: white;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #d10e3c;
        }
        .stButton button:active {
            background-color: #b00a31;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # List of available cuisines
    cuisines = [
        "Mediterranean", "Italian", "Mexican", "Indian", "Chinese", "Japanese",
        "Thai", "French", "Greek", "Spanish", "American", "Middle Eastern",
        "Vietnamese", "Korean", "Brazilian", "Caribbean"
    ]
    
    st.image('logo.png', width=200)
    st.header("Welcome to Recipe Spoonly")
    st.write("           ")
    st.write("           ")
    st.markdown('<h3 style="text-align:center;">A perfect answer to "What to cook today!"</h3>', unsafe_allow_html=True)

    # Text prompt
    st.write("Insert your image:")

    # Option to insert image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg"])

    if uploaded_file is not None:
        with st.spinner("Uploading and processing image..."):
            img_path = save_uploaded_file(uploaded_file)
            if img_path:
                st.session_state.uploaded_image = img_path

    # Cuisine selection
    st.write("Select the cuisine:")
    selected_cuisine = st.selectbox(" ", cuisines)

    if selected_cuisine:
        st.session_state.cuisine = selected_cuisine

    # Process and display recipes
    if st.session_state.uploaded_image and st.session_state.cuisine:
        with st.spinner("Generating recipes..."):
            ing2, ing1 = wk.runninng(st.session_state.uploaded_image)
            recipes = wk.recipie_names(ing2, ing1, st.session_state.cuisine)

        st.write("Select the recipe:")
        selected_recipe = st.selectbox(" ", recipes)

        if selected_recipe:
            with st.spinner("Fetching the recipe..."):
                recipe = wk.generate_recipie(selected_recipe)
                st.write("Here is your recipe:")
                st.write(recipe)

if __name__ == "__main__":
    main()
