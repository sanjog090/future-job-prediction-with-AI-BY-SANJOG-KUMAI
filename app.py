import streamlit as st
from model import predict_job  # Your existing model.py

st.title("💼 Job Predictor AI")

st.write("Select your skills and experience to get a job prediction:")

# Skill checkboxes
python_skill = st.checkbox("Python")
java_skill = st.checkbox("Java")
html_skill = st.checkbox("HTML")
css_skill = st.checkbox("CSS")
ml_skill = st.checkbox("Machine Learning")

# Experience slider
experience = st.slider("Years of Experience", 0, 10, 1)

# Predict button
if st.button("Predict Job"):
    job = predict_job(
        python=int(python_skill),
        java=int(java_skill),
        html=int(html_skill),
        css=int(css_skill),
        ml=int(ml_skill),
        experience=experience
    )
    st.success(f"Predicted Job: {job}")
