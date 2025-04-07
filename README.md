# Sentiment Analysis API

A lightweight Flask API for sentiment analysis using Hugging Face's transformers pipeline.

## Features
- Text sentiment classification (**POSITIVE**/**NEGATIVE**)
- Confidence scoring (0-1 range)
- Version tracking and changelog
- Simple RESTful endpoints
- Robust error handling
- Health check monitoring

## Table of Contents
- [Quick Start](#quick-start)
- [API Endpoints](#api-endpoints)
- [Development Setup](#development-setup)
- [Testing](#testing)
- [Versioning](#versioning)
- [Deployment](#deployment)

## Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

git clone https://github.com/UsamaIbrahim98/sentiment-analysis-api.git
cd sentiment-analysis-api
pip install -r requirements.txt
Running the API
Copy
python app.py
The API will start at http://localhost:5000

### API Endpoints
## Analyze Text
# POST /analyze

bash
Copy
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"I love this API!"}'
# Response:

json
Copy
{
  "sentiment": "POSITIVE",
  "confidence": 0.9998,
  "version": "1.1.0"
}
## Check Version
# GET /version

h
Copy
curl http://localhost:5000/version
## View Changelog
# GET /changelog


Copy
curl http://localhost:5000/changelog
## Health Check
# GET /health


Copy
curl http://localhost:5000/health
### Development Setup
## Create virtual environment:


Copy
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install development requirements:


Copy
pip install -r requirements.txt
## Testing
# Manual Testing
Test the API using curl or Postman with various inputs:


Copy
 Test happy path
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"text":"This is great!"}'

 Test error handling
curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"text":""}'
# Automated Tests
(Include if you have test scripts)

## Versioning
We follow Semantic Versioning:

Check current version: /version endpoint

View changes: /changelog endpoint

Version format: MAJOR.MINOR.PATCH

## Deployment
Production Deployment with Waitress

Copy
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:appwrite