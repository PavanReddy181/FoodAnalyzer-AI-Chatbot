import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image

# Load environment variables
load_dotenv()

# Importing and configuring Google generative AI
try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except ImportError:
    st.error("Failed to import google.generativeai. Make sure it is installed and configured correctly.")

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="FoodAnalyzer AI")

st.header("FoodAnalyzer AI")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose your food image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# User dietary goals input
goal = st.selectbox("Do you want to lose or gain weight?", ["none", "loss", "gain"])
weight = None
target_weight = None
gender = None

if goal in ["loss", "gain"]:
    weight = st.number_input("Your weight in kgs:", min_value=0)
    target_weight = st.number_input("Your target weight in kgs:", min_value=0)
    gender = st.selectbox("Are you male or female?", ["male", "female"])

submit = st.button("Tell me the total calories")

# Improved Prompt with conditional logic based on user inputs
input_prompt = """
You are a highly skilled nutritionist and dietitian. Analyze the food items in the uploaded image and provide a detailed report that includes the following information:

1. Identify each food item in the image.
2. Provide an estimated weight for each food item in grams.
3. Provide the calorie count for each food item.
4. Break down the macronutrients (carbohydrates, proteins, fats) for each item.
5. Assess the total calorie intake and compare it with the daily recommended intake for a balanced diet.
6. Suggest healthier alternatives or adjustments if the calorie count is too high.
7. Evaluate if the meal is suitable for specific dietary goals such as weight loss, muscle gain, or maintenance.
8. Offer tips to improve the nutritional value of the meal.

Format your response as follows:

1. **Item 1: [Food Item]**
   - Estimated Weight: [Number] grams
   - Calories: [Number] kcal
   - Carbohydrates: [Number] g
   - Proteins: [Number] g
   - Fats: [Number] g
   - Notes: [Additional comments]
2. **Item 2: [Food Item]**
   - Estimated Weight: [Number] grams
   - Calories: [Number] kcal
   - Carbohydrates: [Number] g
   - Proteins: [Number] g
   - Fats: [Number] g
   - Notes: [Additional comments]
----
----
**Total Calories: [Number] kcal**

**Assessment:**
[Detailed assessment of the meal's suitability for dietary goals]

**Suggestions:**
[Healthier alternatives or adjustments]

**Tips:**
[General tips to improve nutritional value]
"""

if goal in ["loss", "gain"]:
    input_prompt += f"""
    
**User Details:**
- Goal: {goal}
- Current Weight: {weight} kgs
- Target Weight: {target_weight} kgs
- Gender: {gender}

**Customized Assessment:**
Based on the user's goal to {goal} weight, current weight of {weight} kgs, target weight of {target_weight} kgs, and gender being {gender}, provide tailored suggestions for their dietary plan. If the total calories are too high or too low for their goal, recommend specific food items to remove or add. Also, offer tips on how to balance their macronutrient intake for optimal results.
"""

# If submit button is clicked
if submit:
    if uploaded_file is not None and input:
        with st.spinner("Processing..."):
            try:
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_response(input_prompt, image_data, input)
                st.subheader("The Response is")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload an image and enter a prompt.")

# History Section
if "history" not in st.session_state:
    st.session_state.history = []

if submit and 'response' in locals():
    st.session_state.history.append({"input": input, "response": response, "image": uploaded_file})

if st.sidebar.checkbox("Show History"):
    st.sidebar.subheader("Previous Analyses")
    for i, record in enumerate(st.session_state.history):
        st.sidebar.markdown(f"### Analysis {i+1}")
        st.sidebar.markdown(f"**Prompt:** {record['input']}")
        st.sidebar.markdown(f"**Response:** {record['response']}")
        st.sidebar.image(record['image'], caption="Uploaded Image", use_column_width=True)

