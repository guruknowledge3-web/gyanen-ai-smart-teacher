import streamlit as st
from google import genai
import time

# Configure API
client = genai.Client(
    api_key=st.secrets["GOOGLE_API_KEY"]
)

# Page config
st.set_page_config(page_title="Gyanen AI Smart Teacher")

# Title
st.title("🎓 Gyanen AI Smart Teacher")
st.write("AI-powered multilingual learning assistant using Gemma.")

# Input
topic = st.text_input("Enter Topic:", "Electric Charges")

generate_explanation = st.checkbox("Generate Explanation")
generate_mcqs = st.checkbox("Generate MCQs")
generate_script = st.checkbox("Generate Video Script")

# AI function (ONLY ONE FUNCTION)
def generate_ai_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt
        )
        return response.text

    except Exception:
        return "⚠️ API limit reached. Please wait 1–2 minutes and try again."

# Button
if st.button("Generate"):

    time.sleep(2)  # prevents rapid API calls

    if generate_explanation:
        st.subheader("📘 Explanation")

        prompt = f"""
Explain the topic {topic} for Class 12 students.

Use Hindi + English.
Include examples and important points.
"""

        response = generate_ai_response(prompt)
        st.write(response)

    if generate_mcqs:
        st.subheader("📝 MCQs")

        prompt = f"""
Generate 5 MCQs on topic {topic}
for Class 12 students.

Include answers.
"""

        response = generate_ai_response(prompt)
        st.write(response)

    if generate_script:
        st.subheader("🎬 Video Script")

        prompt = f"""
Create a YouTube teaching script
on topic {topic}
in Hindi + English.
"""

        response = generate_ai_response(prompt)
        st.write(response)
