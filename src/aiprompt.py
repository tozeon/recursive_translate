LANG_SRC_MAP = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Arabic": "ar",
    "Hindi": "hi",
    "Bengali": "bn",
    "Indonesian": "id",
    "Urdu": "ur",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Thai": "th",
    "Persian": "fa",
    "Polish": "pl",
    "Dutch": "nl",
    "Malay": "ms",
    "Greek": "el",
    "Hebrew": "he",
    "Swedish": "sv",
    "Ukrainian": "uk",
    "Finnish": "fi",
    "Czech": "cs",
    "Hungarian": "hu"
}

# SOURCE_LANG = ""
# SOURCE_CODE = ""
# TARGET_LANG = ""
# TEXT = ""

prompt = '''You are a professional {SOURCE_LANG} ({SOURCE_CODE}) to {TARGET_LANG} ({TARGET_CODE}) translator. Your goal is to accurately convey the meaning and nuances of the original {SOURCE_LANG} text while adhering to {TARGET_LANG} grammar, vocabulary, and cultural sensitivities.
Produce only the {TARGET_LANG} translation, without any additional explanations or commentary. Please translate the following {SOURCE_LANG} text into {TARGET_LANG}:

{TEXT}
'''

def generate_prompt(o_lang: int, t_lang: int, text: str):
    return prompt.format(SOURCE_LANG=o_lang, SOURCE_CODE=LANG_SRC_MAP[o_lang], TARGET_LANG=t_lang, TARGET_CODE=LANG_SRC_MAP[t_lang], TEXT=text)
