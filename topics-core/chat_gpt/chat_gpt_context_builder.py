from model.message import Message

COMMAND = 'Summarize the conversation so far in 40 words maximum. Focus the customer sentiment'


def __add_command(messages: []) -> []:
    command_message = Message(content=COMMAND, role="user")
    messages.append(command_message)
    return messages


def configure(messages: []) -> []:
    return __add_command(messages)


