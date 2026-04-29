import streamlit as st

st.set_page_config(page_title="Gyanen AI Smart Teacher")

st.title("🎓 Gyanen AI Smart Teacher")
st.write("AI-powered multilingual learning assistant using Gemma.")

# Topic input
topic = st.text_input("Enter Topic:", "Electric Charges")

# Options
generate_explanation = st.checkbox("Generate Explanation")
generate_mcqs = st.checkbox("Generate MCQs")
generate_script = st.checkbox("Generate Video Script")

# Generate button
if st.button("Generate"):
    
    if generate_explanation:
        st.subheader("📘 Explanation")
        st.write(
            f"Explanation for topic: {topic}\n\n"
            "This section will generate explanation using Gemma model."
        )
    
    if generate_mcqs:
        st.subheader("📝 MCQs")
        st.write(
            f"MCQs for topic: {topic}\n\n"
            "This section will generate MCQs using Gemma model."
        )
    
    if generate_script:
        st.subheader("🎬 Video Script")
        st.write(
            f"Video Script for topic: {topic}\n\n"
            "This section will generate teaching scripts."
        )
