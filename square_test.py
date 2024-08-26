import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

# Load environment variables
load_dotenv()

# Initialize the Slack app
slack_app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Initialize Flask app
flask_app = Flask(__name__)
handler = SlackRequestHandler(slack_app)

# Command handler
@slack_app.command("/square")
def square_number(ack, command):
    ack()
    try:
        number = int(command['text'])
        result = number ** 2
        response = f"The square of {number} is {result}"
    except ValueError:
        response = "Please provide a valid number."
    
    slack_app.client.chat_postMessage(channel=command['channel_id'], text=response)

# Flask route for Slack events
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# Home route
@flask_app.route("/", methods=["GET"])
def home():
    return "Your Slack Bot Server is running!"

# Slack challenge handler
@flask_app.route("/slack/events", methods=["POST"])
def slack_challenge():
    # Check if it's a challenge request
    if "challenge" in request.json:
        return jsonify({"challenge": request.json["challenge"]})
    
    # If it's not a challenge, pass to the regular event handler
    return handler.handle(request)

# We don't need the if __name__ == "__main__" block anymore
# Gunicorn will handle running the app