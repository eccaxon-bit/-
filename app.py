from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def home():
    return "ECCAXON-BIT Running - 01114082665"
@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == "talaq_bila_nezaa_2026":
        return challenge
    return "error"
@app.route("/webhook", methods=["POST"])
def hook():
    return "ok", 200
