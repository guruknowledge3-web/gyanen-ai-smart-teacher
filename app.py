import streamlit as st
from google import genai

# Configure API Key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load model (NEW working model)
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def generate_ai_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt
    )
    return response.text

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

# AI function
def generate_ai_response(prompt):
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.5,
                "max_output_tokens": 300
            }
        )
        return response.text

    except Exception as e:
        return "⚠️ API limit reached. Please wait 1–2 minutes and try again."

# Button
if st.button("Generate"):

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
