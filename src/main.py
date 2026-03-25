from ollama import chat, ChatResponse
from aiprompt import generate_prompt, LANG_SRC_MAP
from random import randint

file_content = ""

with open("./input.txt", "r", encoding='utf-8') as file:
    file_content = r"\n".join(file.readlines())

exe_times = ""
while not exe_times.isdigit():
    exe_times = input("Enter the number of times to recursively translate: ")

exe_times = int(exe_times)

langs = list(LANG_SRC_MAP.keys())

# uncomment and replace as needed
last_lang = input("What is the language of the original text you wish to translate? ")
r_lang = input("What is the final resulting language you wish to translate into? ")
# last_lang = "Chinese"
# r_lang = "English"

for i in range(exe_times-1):
    rand_lang = langs[randint(0,len(langs)-1)]

    prompt=generate_prompt(last_lang, rand_lang, file_content)
    response: ChatResponse = chat(
        model='translategemma',
        messages=[{'role': 'user', 'content': prompt}],
    )
    last_lang = rand_lang
    file_content = response["message"]["content"]
    print("Iteration",i,":",file_content)

prompt=generate_prompt(last_lang, r_lang, file_content)
response: ChatResponse = chat(
    model='translategemma',
    messages=[{'role': 'user', 'content': prompt}],
)
file_content = response["message"]["content"]
print("\n\nFinal translation:\n", file_content)

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(file_content)

print("Saved into \'output.txt\'")