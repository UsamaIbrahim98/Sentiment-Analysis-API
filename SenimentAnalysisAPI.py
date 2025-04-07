
from flask import Flask, jsonify, request
from transformers import pipeline


__version__ = "1.0.1"  
SERVICE_NAME = "Sentiment Analysis API"

app = Flask(__name__)
classifier = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze text sentiment"""
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Text is required"}), 400
    
    result = classifier(text)[0]
    return jsonify({
        "sentiment": result['label'],
        "confidence": float(result['score']),
        "version": __version__
    })

@app.route('/version')
def version():
    """Check current version"""
    return jsonify({
        "service": SERVICE_NAME,
        "version": __version__,
        "status": "running"
    })

@app.route('/changelog')
def changelog():
    """Show recent changes (from CHANGELOG.md)"""
    try:
        with open('CHANGELOG.md', 'r') as f:
            return f.read().replace('\n', '<br>')
    except FileNotFoundError:
        return "Changelog not available", 404

if __name__ == '__main__':
    print(f"Starting {SERVICE_NAME} v{__version__}")
    app.run(host='0.0.0.0', port=5000)