import numpy as np
import pickle
import os
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from src.config import MAX_SEQUENCE_LENGTH, TOKENIZER_PATH, VOCAB_SIZE


def load_corpus(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    return text


def create_sequences(text):
    tokenizer = Tokenizer(num_words=VOCAB_SIZE, oov_token="<OOV>")
    tokenizer.fit_on_texts([text])

    total_words = min(VOCAB_SIZE, len(tokenizer.word_index) + 1)

    input_sequences = []

    for line in text.split("\n"):
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)

    if len(input_sequences) == 0:
        raise ValueError("No sequences generated. Check corpus.txt content.")

    input_sequences = pad_sequences(
        input_sequences,
        maxlen=MAX_SEQUENCE_LENGTH,
        padding='pre'
    )

    X = input_sequences[:, :-1]
    y = input_sequences[:, -1]

    os.makedirs("models", exist_ok=True)

    with open(TOKENIZER_PATH, "wb") as f:
        pickle.dump(tokenizer, f)

    return X, y, total_words
