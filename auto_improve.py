import google.generativeai as genai
import os

# Securely grabs the key from the cloud later
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

file_to_improve = "my_script.py"

# --- NEW DASHBOARD CODE ---
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dashboard = f"""
        <html>
          <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f0f2f5;">
            <h1 style="color: #2e7d32;">✅ Gemini Automation is Active</h1>
            <h2>Your code was successfully improved!</h2>
            <p style="font-size: 18px;"><strong>Last Updated:</strong> {now}</p>
            <p style="color: #666;">Running flawlessly in the background every 20 minutes.</p>
          </body>
        </html>
        """
        with open("index.html", "w") as dash_file:
            dash_file.write(dashboard)
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
