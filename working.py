from ultralytics import YOLOv10
from inference_sdk import InferenceHTTPClient
import os 
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
generate_model = genai.GenerativeModel('gemini-1.5-flash')

def runninng(image):
    models = ['bes.pt', 'FCDETECT.pt', 'm1.pt', 'm2.pt', 'm3.pt']
    results = []
    for  model in models:
        yolo_model = YOLOv10(model)
        ress  = yolo_model.predict(image, conf=0.25)
        results.extend((ress[0].names.values()))
    results2 = []
    CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="LldEGIHZ7ZlAJOqQCsNV"
    )
    r1 = CLIENT.infer(image, model_id="aicook-lcv4d/3")
    d = []
    li = r1["predictions"]
    for each in li:
        d.append(each['class']) 
    results2.append(list(set(d)))
    CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="LldEGIHZ7ZlAJOqQCsNV"
    )
    r2 = CLIENT.infer(image, model_id="detec-ingredients-2/1")
    d = []
    li = r2["predictions"]
    for each in li:
        d.extend(each['class']) 
    results2.append(list((d)))
    return list(set(results)),results2
def recipie_names(results,results2,cuisine):
    prompt = f"""
    You are a recipe generator that can create recipes based on two lists of ingredients and a specified cuisine. The generator should prioritize using ingredients from the first list. If additional ingredients are needed to complete the recipe, it should use ingredients from the second list. 
    The generator should also consider the input cuisine type and provide an estimated cooking time for each suggested recipe. Please return only the names of the possible recipes along with their cooking times in brackets, accept all forms of input and do not give suggestions rather estimated output.
    DO not show INPUT in the resluts
    Input:
    1. Primary Ingredients: {results2}
    2. Secondary Ingredients: {results}
    3. Cuisine: {cuisine}
    Output:[ list of Recipe Name (Cooking Time)]
    ---
    Example Prompt
    Input:
    1. Primary Ingredients: [Chicken breast, Garlic, Olive oil, Lemon, Salt, Black pepper]
    2. Secondary Ingredients: [Thyme, Rosemary, Paprika, Butter, Honey, Onion]
    3. Cuisine: Mediterranean
    Output:
    [Mediterranean Lemon Garlic Chicken (35 minutes),Garlic Herb Butter Chicken (40 minutes),Mediterranean Chicken with Honey Lemon Glaze (45 minutes)]
    """
    
    response = generate_model.generate_content(prompt)
    text = response.text
    cleaned_string = text.replace('[', '').replace(']', '')
    result_list = [item.strip() for item in cleaned_string.split(',')]
    return result_list
def generate_recipie(dish_name):
    prompt = f"you are a great chef with amazing and tasty recipies, your task is to generate recipie of {dish_name}"
    response = generate_model.generate_content(prompt)
    return response.text

