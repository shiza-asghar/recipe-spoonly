# Recipe Spoonly

Welcome to **Recipe Spoonly**, a recipe recommendation system for your fridge! This application allows you to upload an image of your ingredients and select a cuisine type to receive personalized recipe suggestions.

## Features

- **Image Upload**: Upload an image of your ingredients.
- **Cuisine Selection**: Choose from a list of various cuisines.
- **Recipe Generation**: Get recipe suggestions based on the uploaded image and selected cuisine.
- **Recipe Display**: View detailed recipes with cooking instructions.

## Technologies Used

- **Python**: The main programming language.
- **Streamlit**: Framework for creating the web application.
- **PIL (Pillow)**: For image processing.
- **YOLOv10**: Used for ingredient detection in images.
- **Roboflow**: Used to streamline the model training and deployment process.
- **Custom Working Module (`working`)**: Contains the logic for processing images and generating recipes.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/recipe-spoonly.git
    cd recipe-spoonly
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add Your Logo**:
    Ensure you have a logo image named `logo.png` in the project directory.

## Usage

1. **Run the Application**:
    ```bash
    streamlit run recipe_app.py
    ```

2. **Navigate to the URL**:
    Open the URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.

3. **Upload an Image**:
    - Click on "Choose an image..." and upload a JPEG image of your ingredients.
    - The uploaded image will be displayed on the page.

4. **Select a Cuisine**:
    - Choose a cuisine type from the dropdown menu.
    - Recipe suggestions will be generated based on the ingredients and selected cuisine.

5. **View and Select a Recipe**:
    - Select a recipe from the generated list.
    - Detailed cooking instructions for the selected recipe will be displayed.

## File Structure

```plaintext
recipe-spoonly/
├── training/               # Contains the code and model for traning
├── tester/                 # Contains the images for testing
├── uploads/                # Directory for uploaded images
├── logo.png                # Logo image file
├── requirements.txt        # List of Python packages required
├── recipe_app.py           # Main application code
├── working.py              # Custom module for processing and generating recipes
├── *.pt                    # custom trained yolo  models 
└── README.md               # This README file
