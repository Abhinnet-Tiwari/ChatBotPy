

# from flask import Flask, request, jsonify
# from transformers import pipeline
# from flask_cors import CORS  

# app = Flask(__name__)
# CORS(app, resources={r"/ask": {"origins": "*"}})

# # Use a better chatbot model
# chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

# @app.route('/')
# def index():
#     return "Welcome to the Improved Chatbot API!"

# @app.route('/ask', methods=['POST'])
# def ask():
#     data = request.get_json()
#     user_input = data.get("message")

#     if not user_input:
#         return jsonify({"error": "No message provided"}), 400

#     # Generate chatbot response
#     response = chatbot(user_input, max_length=200, num_return_sequences=1)

#     return jsonify({"response": response[0]['generated_text']})

# if __name__ == '__main__':
#     app.run(debug=True)


import os
from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS  

app = Flask(__name__)
CORS(app, resources={r"/ask": {"origins": "*"}})

chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

@app.route('/')
def index():
    return "Welcome to the Improved Chatbot API!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = chatbot(user_input, max_length=200, num_return_sequences=1)

    return jsonify({"response": response[0]['generated_text']})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's PORT
    app.run(host="0.0.0.0", port=port, debug=True)
