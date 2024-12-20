# Food Locha 🍴

Food Locha is a user-friendly Streamlit-based web application that uses Google Gemini Pro Vision API to analyze meal images, calculate calorie details, and provide nutritional insights. The application supports image uploads in formats such as PNG, JPEG, and HEIC, and offers the option to translate results into multiple languages.

## Features
- **Image Upload & Conversion:** Supports PNG, JPEG, and HEIC image formats.
- **Calorie Estimation:** Leverages Google Gemini Pro Vision API to identify food items and calculate calorie counts.
- **Language Translation:** Translates results into multiple languages using `googletrans`.
- **Interactive UI:** Built with Streamlit for an intuitive and responsive user interface.

## Live Demo
Try the app here: [Food Locha](https://healthmanagementapp.streamlit.app/)

## Installation

### Prerequisites
- Python 3.8 or above
- A Google Cloud API key with access to the Gemini Pro Vision API

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rebel47/food-locha.git
   cd food-locha
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## How It Works
1. **Image Processing:** Uploaded images are converted to JPEG format for compatibility.
2. **Content Analysis:** Google Gemini Pro Vision API identifies food items and their calorie content.
3. **Translation:** The response is translated into the selected language using `googletrans`.
4. **Output Display:** Calorie details and nutritional suggestions are displayed in the chosen language.

## Usage
1. **Input:** Upload a meal image and optionally ask a specific question.
2. **Language Selection:** Choose the language for the output (English, French, Dutch, or German).
3. **Calorie Analysis:** Click on the button to process and retrieve results.

## Example Output
```
1. Apple - 95 calories
2. Rice - 206 calories
3. Chicken - 335 calories
----
Suggestions:
1. Add more greens to your meal.
2. Reduce sugar intake for better health.
```

## Technologies Used
- **Streamlit:** For the interactive web interface
- **Pillow & pillow-heif:** For image processing and HEIC support
- **Google Gemini Pro Vision API:** For image analysis and calorie estimation
- **googletrans:** For language translation
- **Python-dotenv:** For environment variable management

## Future Enhancements
- Add more output language options.
- Enhance calorie estimation accuracy with additional datasets.
- Include a food database for offline calorie calculations.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- **Google Cloud:** For their powerful APIs
- **Streamlit:** For simplifying web application development

---

**Made with ❤️ by Ayaz**
