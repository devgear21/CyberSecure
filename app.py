
from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = openai.Completion.create(
        model="text-davinci-003",  # You can choose the model
        prompt="Network Anomaly Detection: " + user_input,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug=True)
