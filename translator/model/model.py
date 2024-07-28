
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import logging

# Load Tokenizers
with open('./model/tokenizer_eng.pkl', 'rb') as file:
    tokenizer_eng = pickle.load(file)

with open('./model/tokenizer_fr.pkl', 'rb') as file:
    tokenizer_fr = pickle.load(file)

max_seq_len_eng = 15  # Set the maximum sequence length

class Translator:
    def __init__(self, model_path):
        logging.info("Translator class initialized")
        self.model = load_model(model_path)
        logging.info("Model is loaded!")

    def process_input(self, sentence):
        # Tokenize and pad the input sentence
        sequence = tokenizer_eng.texts_to_sequences([sentence])
        padded_sequence = pad_sequences(sequence, maxlen=max_seq_len_eng, padding='post')
        return padded_sequence

    def translate(self, padded_sequence):
        # Predict the sequence
        predictions = self.model.predict(padded_sequence)
        return predictions

    def process_output(self, predictions):
        # Convert predictions to words
        predicted_words = [tokenizer_fr.index_word.get(np.argmax(pred), '') for pred in predictions[0]]

        # Remove padding tokens
        predicted_words = [word for word in predicted_words if word != '']
        return ' '.join(predicted_words)

    def translate_sentence(self, sentence):
        try:
            padded_sequence = self.process_input(sentence)
            predictions = self.translate(padded_sequence)
            translated_sentence = self.process_output(predictions)
            return translated_sentence
        except Exception as e:
            logging.error(f"Error in translation: {e}")
            return "Translation error occurred"

