from transformers import pipeline
from flask import Flask, request

app = Flask(__name__)

classifier = pipeline("text-classification")


@app.post("/classify-text")
def classify_text():
    if request.is_json:
        data = request.json
        text = data.get("text", "")
        return {'results': classifier(text)}
    else:
        return "Content type not supported", 400
