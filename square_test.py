import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

# Load environment variables
load_dotenv()

# Initialize the Slack app
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Initialize Flask app
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# Command handler
@app.command("/square")
def square_number(ack, command):
    ack()
    try:
        number = int(command['text'])
        result = number ** 2
        response = f"The square of {number} is {result}"
    except ValueError:
        response = "Please provide a valid number."
    
    app.client.chat_postMessage(channel=command['channel_id'], text=response)

# Flask route for Slack events
@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# Home route
@flask_app.route("/", methods=["GET"])
def home():
    return "Your Slack Bot Server is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)
