import os
from sys import argv

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def send_message(body, to_text):
    client = Client(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])
    message = client.messages.create(
        to=to_text, 
        from_=os.environ['ACCOUNT_PHONE'],
        body=body)
    print(message.sid)

if __name__ == "__main__":
    send_message("Hello from Python!", argv[1])