from src.predict import predict_next_word

while True:
    text = input("Enter text: ")
    print("Next word:", predict_next_word(text))
