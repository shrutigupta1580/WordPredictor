import os
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from src.data_loader import load_corpus, create_sequences
from src.model import build_model
from src.config import MODEL_PATH, EPOCHS, BATCH_SIZE


def train_model():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    corpus_path = os.path.join(base_dir, "data", "corpus.txt")

    text = load_corpus(corpus_path)
    X, y, total_words = create_sequences(text)

    print("Training samples:", X.shape[0])
    print("Vocabulary size:", total_words)

    model = build_model(total_words)

    checkpoint = ModelCheckpoint(
        MODEL_PATH,
        monitor='val_loss',
        save_best_only=True,
        verbose=1
    )

    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True
    )

    model.fit(
        X, y,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        validation_split=0.1,
        callbacks=[checkpoint, early_stop]
    )


if __name__ == "__main__":
    train_model()
