import chat_gpt_context_builder
import chat_gpt_service
import chat_gpt_messages_parser
import time

messages = chat_gpt_messages_parser.build_conversation("6.txt")
amount_of_messages = len(messages)
i = 0
while i <= amount_of_messages:
    messages_subset = messages[0:i+2]
    messages_subset = chat_gpt_context_builder.configure(messages_subset)
    result = chat_gpt_service.send_request(messages_subset)
    print(result)
    time.sleep(21)
    i+=2