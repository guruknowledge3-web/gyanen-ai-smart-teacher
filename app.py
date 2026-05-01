import streamlit as st
from google import genai
import time

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# Configure API
client = genai.Client(
    api_key=st.secrets["GOOGLE_API_KEY"]
)

# Page config
st.set_page_config(page_title="Gyanen AI Smart Teacher")

# Title

st.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
    width=80
)

st.title("🎓 Gyanen AI Smart Teacher")
st.write("AI-powered multilingual learning assistant using Gemma.")

# ---------------- INPUT SECTION ----------------

topic = st.text_input("Enter Topic:", "Electric Charges")

# NEW: Subject selector
subject = st.selectbox(
    "📚 Select Subject",
    ["Physics", "Chemistry", "Biology", "Mathematics"]
)

difficulty = st.selectbox(
    "🎯 Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

language = st.selectbox(
    "🌍 Select Language",
    ["Hindi + English", "English Only"]
)

generate_explanation = st.checkbox("Generate Explanation")
generate_mcqs = st.checkbox("Generate MCQs")
generate_script = st.checkbox("Generate Video Script")
generate_revision = st.checkbox("Generate Revision Notes")

# ---------------- AI FUNCTION ----------------

# ⭐ MOVE PDF FUNCTION HERE (OUTSIDE)

  def generate_ai_response(prompt):

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception:
        return "⚠️ API limit reached."


# PDF Function

def create_pdf(text):

    buffer = BytesIO()

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(buffer)

    story = []

    paragraphs = text.split("\n")

    for line in paragraphs:
        story.append(Paragraph(line, styles["Normal"]))

    pdf.build(story)

    buffer.seek(0)

    return buffer

# ---------------- BUTTON ----------------

 if st.button("Generate"):

    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")
        st.stop()

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

Use {language}.
"""

        response = generate_ai_response(prompt)

        st.write(response)

        # NEW: Download button
         pdf_file = create_pdf(response)

st.download_button(
    label="📄 Download Notes (PDF)",
    data=pdf_file,
    file_name=f"{topic}_notes.pdf",
    mime="application/pdf"
)
    # ---------------- MCQs ----------------

    if generate_mcqs:

        st.subheader("📝 MCQs")
        prompt = f"""
Generate 5 {difficulty} MCQs
on topic {topic}
from subject {subject}
for Class 12 students.

Use {language}.

Include answers.
"""

         response = generate_ai_response(prompt)

        st.write(response)

         pdf_file = create_pdf(response)

st.download_button(
    label="📄 Download MCQs (PDF)",
    data=pdf_file,
    file_name=f"{topic}_mcqs.pdf",
    mime="application/pdf"
)

    # ---------------- VIDEO SCRIPT ----------------

    if generate_script:

        st.subheader("🎬 Video Script") 
        
     prompt = f"""
Create a YouTube teaching script
on topic {topic}
from subject {subject}
for Class 12 students.

Use {language}.

Include:

- Introduction
- Explanation
- Example
- Summary
"""

        response = generate_ai_response(prompt)

        st.write(response)

         pdf_file = create_pdf(response)

st.download_button(
    label="📄 Download Script (PDF)",
    data=pdf_file,
    file_name=f"{topic}_script.pdf",
    mime="application/pdf"
)

# ---------------- REVISION NOTES ----------------

if generate_revision:

    st.subheader("📝 Revision Notes")

    prompt = f"""
Create short revision notes
on topic {topic}
from subject {subject}
for Class 12 students.

Use {language}.

Include:

- Key definitions
- Important formulas
- Bullet points
- Quick revision summary
"""

    response = generate_ai_response(prompt)

    st.write(response)

    # PDF download
    pdf_file = create_pdf(response)

    st.download_button(
        label="📄 Download Revision Notes (PDF)",
        data=pdf_file,
        file_name=f"{topic}_revision_notes.pdf",
        mime="application/pdf"
    )
