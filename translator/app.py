from flask import Flask, request, jsonify,render_template
from model.model import Translator
import logging

logging.basicConfig(level=logging.INFO)

model = Translator('./model/model_bidirectional.h5')

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    if request.method == 'POST':
        input_text = request.form.get("input_text", "")
        if input_text:
            translation = model.translate_sentence(input_text)
    return render_template('index.html', translation=translation)

@app.route("/v1/translate", methods=["POST"])
def translate():
    logging.info("Translate request received!")
    input_text = request.form.get("input_text", "")
    if not input_text:
        return jsonify({"error": "No input text provided"}), 400

    try:
        translation = model.translate_sentence(input_text)
        return jsonify({"translation": translation})
    except Exception as e:
        logging.error(f"Error in translation: {e}")
        return jsonify({"error": "Translation error occurred"}), 500

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


