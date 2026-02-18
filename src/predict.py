import os
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from src.config import MAX_SEQUENCE_LENGTH, MODEL_PATH, TOKENIZER_PATH


model = None
tokenizer = None
index_to_word = None

if os.path.exists(MODEL_PATH) and os.path.exists(TOKENIZER_PATH):
    model = load_model(MODEL_PATH)

    with open(TOKENIZER_PATH, "rb") as f:
        tokenizer = pickle.load(f)

    index_to_word = {index: word for word, index in tokenizer.word_index.items()}


def predict_next_word(seed_text):
    if model is None:
        return "Model not trained yet."

    token_list = tokenizer.texts_to_sequences([seed_text.lower()])[0]
    token_list = pad_sequences([token_list], maxlen=MAX_SEQUENCE_LENGTH - 1, padding='pre')

    predicted_probs = model.predict(token_list, verbose=0)
    predicted_index = np.argmax(predicted_probs, axis=-1)[0]

    return index_to_word.get(predicted_index, "")
