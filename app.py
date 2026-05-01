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

# ---------------- INPUT SECTION ----------------

topic = st.text_input("Enter Topic:", "Electric Charges")

# NEW: Subject selector
subject = st.selectbox(
    "📚 Select Subject",
    ["Physics", "Chemistry", "Biology", "Mathematics"]
)

generate_explanation = st.checkbox("Generate Explanation")
generate_mcqs = st.checkbox("Generate MCQs")
generate_script = st.checkbox("Generate Video Script")

# ---------------- AI FUNCTION ----------------

def generate_ai_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt
        )
        return response.text

    except Exception:
        return "⚠️ API limit reached. Please wait 1–2 minutes and try again."

# ---------------- BUTTON ----------------

if st.button("Generate"):

    time.sleep(2)  # Prevent rapid API calls

    # ---------------- EXPLANATION ----------------

    if generate_explanation:

        st.subheader("📘 Explanation")

        prompt = f"""
Explain the topic {topic}
from subject {subject}
for Class 12 students.

Include:

1. Definition  
2. Important formulas  
3. Real-life examples  
4. Key exam points  

Use simple Hindi + English.
"""

        response = generate_ai_response(prompt)

        st.write(response)

        # NEW: Download button
        st.download_button(
            label="📥 Download Notes",
            data=response,
            file_name=f"{topic}_notes.txt",
            mime="text/plain"
        )

    # ---------------- MCQs ----------------

    if generate_mcqs:

        st.subheader("📝 MCQs")

        prompt = f"""
Generate 5 MCQs on topic {topic}
from subject {subject}
for Class 12 students.

Include answers.
"""

        response = generate_ai_response(prompt)

        st.write(response)

        st.download_button(
            label="📥 Download MCQs",
            data=response,
            file_name=f"{topic}_mcqs.txt",
            mime="text/plain"
        )

    # ---------------- VIDEO SCRIPT ----------------

    if generate_script:

        st.subheader("🎬 Video Script")

        prompt = f"""
Create a YouTube teaching script
on topic {topic}
from subject {subject}
for Class 12 students.

Use Hindi + English.

Include:
- Introduction
- Explanation
- Example
- Summary
"""

        response = generate_ai_response(prompt)

        st.write(response)

        st.download_button(
            label="📥 Download Script",
            data=response,
            file_name=f"{topic}_script.txt",
            mime="text/plain"
        )
