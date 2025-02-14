# A flask based application that accepts a prompt from the user and generates two AI images on the page. Show a loader and reset when a new submission is provided.

from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure OpenAI API key
# openai.api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get JSON data instead of form data
    data = request.get_json()
    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    try:
        response = client.images.generate(prompt=prompt, n=1, size="256x256")
        print(response)
        # Extract just the URLs from the response
        image_urls = [img.url for img in response.data]
        return jsonify({'images': image_urls})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)