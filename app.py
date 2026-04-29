import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Load model (stable working version)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

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
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 1024,
        }
    )
    return response.text

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
