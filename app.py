from flask import Flask, render_template, request, jsonify
from chatbot.nlp_model import get_response  # Import chatbot logic

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')  # ✅ Ensures index.html is found

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = get_response(user_message)  # ✅ Calls the real chatbot function

    # ✅ Debugging: Print response to check if it's working
    print(f"User: {user_message}")
    print(f"Bot: {bot_response}")

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
