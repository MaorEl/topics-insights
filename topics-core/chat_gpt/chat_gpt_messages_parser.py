from model.message import Message

USER_ROLE = 'user'
USER_AGENT = 'assistant'

CUSTOMER_PREFIX = "Customer"
AGENT_PREFIX = "Agent"


def build_conversation(file_path: str) -> []:
    ret_val = []
    with open(file_path) as messages_file:
        messages_lines = messages_file.read().splitlines()
        for message_line in messages_lines:
            splitted_line = message_line.split(": ")
            content = splitted_line[1]
            role = get_speaker_role(splitted_line)
            message = Message(role=role, content=content)
            ret_val.append(message)

    return ret_val


def get_speaker_role(splitted_message):
    speaker = splitted_message[0]
    if speaker == CUSTOMER_PREFIX:
        role = USER_ROLE
    else:
        role = USER_AGENT
    return role
