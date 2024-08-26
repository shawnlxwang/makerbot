import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load environment variables
load_dotenv()

# Initialize the Slack client with your bot token
slack_token = os.getenv("SLACK_TOKEN")
client = WebClient(token=slack_token)

# Specify the channel and message
channel_id = os.getenv("TEST_CHANNEL_ID")
message = "Hello from your Python Slackbot!"

# Send the message
try:
    response = client.chat_postMessage(channel=channel_id, text=message)
    print(f"Message sent: {response['ts']}")
except SlackApiError as e:
    print(f"Error sending message: {e}")