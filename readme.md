# 🧠 Next Word Prediction using BiLSTM (TensorFlow + Streamlit)

A Neural Language Model built from scratch using TensorFlow/Keras that predicts the next word in a sentence.  
The project includes data generation, training pipeline, and a Streamlit web interface.

---

## 🚀 Project Overview

This project implements a word-level language model using:

- Embedding Layer
- Bidirectional LSTM
- Softmax output layer
- Sparse categorical cross-entropy loss

The model learns to predict:

P(next_word | previous_words)

It is trained on 50,000 synthetically generated sentences that include:
- General everyday language
- Conversational phrases
- Technology-related sentences

---

## 🏗 Project Architecture

word_predictor/
│
├── data/
│ └── corpus.txt
│
├── models/
│ ├── model.h5
│ └── tokenizer.pkl
│
├── src/
│ ├── config.py
│ ├── data_loader.py
│ ├── model.py
│ ├── train.py
│ ├── predict.py
│ └── init.py
│
├── generate_dataset.py
├── main_train.py
├── streamlit_app.py
├── requirements.txt
└── README.md


---

## 📊 Model Details

- **Embedding Dimension:** 128  
- **LSTM Units:** 128  
- **Max Sequence Length:** 20  
- **Vocabulary Cap:** 30,000 words  
- **Loss Function:** Sparse Categorical Crossentropy  
- **Optimizer:** Adam  
- **Validation Split:** 10%  
- **Early Stopping Enabled**

---

## 🧪 Dataset

The dataset contains 50,000 synthetically generated sentences combining:

- Everyday conversational phrases  
- Emotional expressions  
- Daily activities  
- Technology-related topics  

Example patterns:

- I am happy  
- I like music  
- I want to play guitar  
- Machine learning transforms modern technology  
- Today I feel excited  

---

## ⚙️ Installation

### 1️⃣ Create Virtual Environment

```bash
conda create -n word python==3.10 -y

Activate:
conda activate word

Deactivate:
conda deactivate

2️⃣ Install Dependencies 
pip install -r requirements.txt


📝 Generate Dataset
python generate_dataset.py


🏋️ Train the Model
python main_train.py


🌐 Run Web App (Streamlit)
streamlit run streamlit_app.py

Author:

Name:- Shruti Gupta
Gmail:-Shrutigupta1580@gmail.com
Github:-https://github.com/shrutigupta1580

Name:- Shreya Sinha
Gmail:-shreyasinha476@gmail.com
Github:-https://github.com/sinha-shreyaa
