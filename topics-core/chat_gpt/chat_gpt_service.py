import json
from dataclasses import asdict
import requests as requests

TIMEOUT = 5000
URL = 'https://api.openai.com/v1/chat/completions'
TOKEN = "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"
HEADERS = {"Content-Type": "application/json",
           "Authorization": f"Bearer {TOKEN}"}
CHAT_GPT_VERSION = "gpt-3.5-turbo"

BODY = {
    "model": f"{CHAT_GPT_VERSION}",
    "messages": [],
    "temperature": 0.2
}


def __build_body(messages):
    ret_val = BODY
    ret_val['messages'] = [asdict(message) for message in messages]
    return ret_val


def send_request(messages: []):
    body = __build_body(messages)
    json_body = json.dumps(body)
    response = requests.post(URL, params=None, headers=HEADERS, data=json_body, timeout=TIMEOUT)
    response.raise_for_status()

    data: dict = json.loads(response.content.decode('UTF-8'))
    return data
