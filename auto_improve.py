import google.generativeai as genai
import os

# Securely grabs the key from the cloud later
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

file_to_improve = "my_script.py"

# Read the current code
with open(file_to_improve, "r") as file:
    current_code = file.read()

# Ask Gemini to improve it
prompt = f"Refactor and improve this code. Return ONLY the raw code, no markdown formatting or explanations:\n\n{current_code}"
response = model.generate_content(prompt)

# Save the new code
if response.text:
    cleaned_code = response.text.strip().replace("```python", "").replace("```", "")
    with open(file_to_improve, "w") as file:
        file.write(cleaned_code)