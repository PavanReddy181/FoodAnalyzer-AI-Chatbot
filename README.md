# 🍽️ FoodAnalyzer AI 🍽️

## Overview 📊

FoodAnalyzer AI is an interactive application that leverages Google Gemini Pro Vision API to analyze food images and provide detailed nutritional information. The app helps users understand the calorie content, macronutrient breakdown, and suitability of meals for specific dietary goals.

## Features 🌟

- Upload a food image and get detailed nutritional information.
- Specify dietary goals (weight loss or gain) for personalized recommendations.
- Receive tips for healthier alternatives and improvements.
- Track history of previous analyses.

## Installation 🛠️

Clone the repository:

```bash
git clone https://github.com/yourusername/FoodAnalyzer-AI.git
cd FoodAnalyzer-AI
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Set up environment variables:

1. Create a `.env` file in the project directory.
2. Add your Google API key to the `.env` file:

    ```bash
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage 🚀

Run the Streamlit app:

```bash
streamlit run app.py
```

### Upload a food image:

Choose an image file (jpg, jpeg, png, webp) of the food you want to analyze.

### Enter your dietary goals:

Select whether you want to lose or gain weight.
Provide your current weight, target weight, and gender if applicable.

### Get detailed nutritional information:

Click on "Tell me the total calories" to process the image and get the analysis.

## How It Works 🔍

1. **Image Upload:** Users can upload an image of their food.
2. **User Input:** Users can specify dietary goals such as weight loss or gain.
3. **API Call:** The app uses the Google Gemini Pro Vision API to analyze the food items in the image.
4. **Detailed Report:** The app provides a detailed nutritional breakdown, including calorie count, macronutrients, and personalized recommendations.

## Insights 🔍

This project offers several key insights:

- **Integration of AI with Nutrition:** By leveraging advanced AI models like **Google Gemini Pro Vision API**, we can bring a new level of precision and detail to nutritional analysis, which can be invaluable for individuals looking to manage their diet more effectively.
  
- **Customization for Personal Goals:** The ability to input personal dietary goals (such as weight loss or gain) allows for a highly personalized user experience. The app can tailor its recommendations to meet individual needs, making the advice more actionable.

- **User-Friendly Interface:** Streamlit provides an intuitive interface that makes it easy for users to interact with the app, upload images, and get instant feedback on their dietary choices.

- **Educational Value:** The detailed breakdown of macronutrients and calorie content for each food item can educate users about the nutritional value of their meals, helping them make healthier choices over time.

- **Potential for Further Development:** This project lays the groundwork for future enhancements, such as integrating more dietary preferences, adding more detailed nutritional metrics, or expanding the types of analyses performed.

## Requirements 📋

- streamlit
- google-generativeai
- python-dotenv

## Example Input Prompt 📝

```text
You are a highly skilled nutritionist and dietitian. Analyze the food items in the uploaded image and provide a detailed report that includes the following information:

1. Identify each food item in the image.
2. Provide an estimated weight for each food item in grams.
3. Provide the calorie count for each food item.
4. Break down the macronutrients (carbohydrates, proteins, fats) for each item.
5. Assess the total calorie intake and compare it with the daily recommended intake for a balanced diet.
6. Suggest healthier alternatives or adjustments if the calorie count is too high.
7. Evaluate if the meal is suitable for specific dietary goals such as weight loss, muscle gain, or maintenance.
8. Offer tips to improve the nutritional value of the meal.
```

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
