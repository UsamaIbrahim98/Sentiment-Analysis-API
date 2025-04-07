#%%
from flask import Flask, jsonify, request
from transformers import pipeline
#%%

#%%
app = Flask(__name__)

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Analyze sentiment
        classifier = pipeline("sentiment-analysis")
        results = classifier(text)
        sentiments = [{"label": result['label'], "score": result['score']} for result in results]
        return jsonify(sentiments)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Congratulations! Your server is working"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# %%
