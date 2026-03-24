from ollama import chat
from aiprompt import prompt

file_content = ""

with open("./text.txt") as file:
    file_content = file.readline()

response = chat(
    model='kimi-k2.5:cloud',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)
print(file_content)