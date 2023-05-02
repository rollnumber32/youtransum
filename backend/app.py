from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")


def fetch_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ""
    for t in transcript:
        text += t["text"]
    return text


def summarize(transcript):
    inputs = tokenizer.encode(
        "summarize: " + transcript, return_tensors="pt", max_length=512, truncation=True
    )
    outputs = model.generate(inputs)
    return tokenizer.decode(
        outputs[0],
        max_length=150,
        min_length=40,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
    )


app = Flask(__name__)


@app.route("/api/summarize/<url>")
def get_summary(url):
    transcript = fetch_transcript(url)
    summary = summarize(transcript)
    return summary


if __name__ == "__main__":
    app.run(host="localhost", port=8000)
