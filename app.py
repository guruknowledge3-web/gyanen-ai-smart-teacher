import streamlit as st
import requests

st.set_page_config(page_title="Gyanen AI Smart Teacher")

st.title("🎓 Gyanen AI Smart Teacher")
st.write("AI-powered multilingual learning assistant using Gemma.")

topic = st.text_input("Enter Topic:", "Electric Charges")

generate_explanation = st.checkbox("Generate Explanation")
generate_mcqs = st.checkbox("Generate MCQs")
generate_script = st.checkbox("Generate Video Script")

def generate_ai_response(prompt):
    # Placeholder for AI integration
    return f"AI Response for: {prompt}"

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
