from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from src.config import EMBEDDING_DIM, LSTM_UNITS, MAX_SEQUENCE_LENGTH


def build_model(total_words):
    model = Sequential([
        Embedding(total_words, EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH - 1),
        Bidirectional(LSTM(LSTM_UNITS)),
        Dropout(0.2),
        Dense(total_words, activation='softmax')
    ])

    model.compile(
        loss='sparse_categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    return model
