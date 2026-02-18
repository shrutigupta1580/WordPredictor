import streamlit as st
from src.predict import predict_next_word

st.set_page_config(page_title="Next Word Predictor", layout="centered")

st.title("Next Word Prediction App")
st.write("Enter a sentence and get the predicted next word.")

user_input = st.text_input("Enter text:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        next_word = predict_next_word(user_input)
        st.success(f"Predicted Next Word: {next_word}")
