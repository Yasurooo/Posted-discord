import requests
import time
import json
from datetime import datetime

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN = config['TOKEN']
CHANNELS = config['CHANNELS']
LOG_WEBHOOK_URL = config['LOG_WEBHOOK_URL']
EMOJI = config['EMOJIS']

Status_Emoji = EMOJI['Status_Emoji']
Uptime_Emoji = EMOJI['Uptime_Emoji']
Channel_Emoji = EMOJI['Channel_Emoji']
Logs_Emoji = EMOJI['Logs_Emoji']

# Start time (for uptime tracking)
start_time = datetime.now()

# Initialize message count
message_count = 0

def format_uptime(start_time):
    uptime_duration = datetime.now() - start_time
    days = uptime_duration.days
    hours, remainder = divmod(uptime_duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

def send_message(content, channel_id, delay):
    global message_count
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'Authorization': TOKEN,
        'Content-Type': 'application/json',
    }

    json_data = {
        'content': content,
    }

    response = requests.post(url, headers=headers, json=json_data)

    if response.status_code == 200:
        message_count += 1
        log_message(f"Message sent successfully to <#{channel_id}>.", channel_id=channel_id)
    elif response.status_code == 401:
        print("Unauthorized: Check your token and permissions.")
        print(f"Response: {response.text}")
    elif response.status_code == 429:
        retry_after = response.json().get('retry_after', 0) / 1000
        print(f"Rate limit hit! Retrying after {retry_after:.2f} seconds.")
        time.sleep(retry_after)
        send_message(content, channel_id, delay)
    else:
        log_message(f"Failed to send message: {content} - Status Code: {response.status_code} - {response.text}",
                    status="Error", channel_id=channel_id)
                    
def log_message(log_content, status="Success", channel_id=None):
    log_embed = {
        "title": f"{Status_Emoji} Log : {status}",
        "color": 13882323 if status == "Success" else 11119017,
        "fields": [
            {
                "name": f"{Uptime_Emoji} **Uptime**",
                "value": format_uptime(start_time),
                "inline": True
            },
            {
                "name": f"{Channel_Emoji} **Channel**",
                "value": f"<#{channel_id}>" if channel_id else "N/A",
                "inline": True
            },
            {
                "name": f"{Logs_Emoji}**Log Content**",
                "value": log_content,
                "inline": True
            }
        ],
        "footer": {
            "text": "Auto Post Logs",
            "icon_url": "https://cdn.discordapp.com/attachments/1287019453921493103/1292401890813939764/images_1.jpg"
        },
        "timestamp": str(datetime.now())
    }

    log_data = {
        "embeds": [log_embed],
        "username": "Auto Post Logs"
    }

    response = requests.post(LOG_WEBHOOK_URL, json=log_data)

    if response.status_code == 204:
        print(f"Log sent successfully to channel ID: {channel_id}!")
    else:
        print(f"Failed to send log: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("Starting loop...")
    while True:
        for channel in CHANNELS:
            channel_id = channel['id']
            delay = channel['delay']
            message = channel['message']
            print(f"Sending message to channel ID: {channel_id} with delay: {delay} minutes")
            send_message(message, channel_id, delay)
            print(f"Sleeping for {delay} minutes before sending to the next channel...")
            time.sleep(delay * 60)