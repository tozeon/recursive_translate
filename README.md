# LLM Recursive Translator

## Description

This is an small python application that recursively translates text a certain number of specified times before translating back into a given language.

## How it works

It uses translategemma to translate text multiple times and outputs it into `output.txt`. It will repeatedly feed its own output into itself until the specified number of times is reached. Then it will translate the resulting input one more time into the desired output language.

## Note

Due to the use of an LLM, the results will usually be more accurate than if you used something like Google translate. This typically means the translation will be closer to the original message and it'll also usually be less funny compared to if Google translate was used.

## Installation

### ***Prerequistes***

- [Python](https://www.python.org/downloads/) latest (for manual)
- [Ollama](https://ollama.com/)
- [TranslateGemma](https://ollama.com/library/translategemma)

### Manual
1. Clone the repository with `git clone <project url>`.
2. Change directory into the cloned repository.
3. Change the contents of `input.txt` as needed.
4. Create a virtual environment to isolate dependencies: `python3 -m venv venv # Use "python" instead of "python3" if needed`
- Activate the virtual environment:
- **Windows (Command Prompt/PowerShell):**
```bash
.\venv\Scripts\activate
```
- **macOS/Linux:**
```bash
source venv/bin/activate
```
*(Your terminal prompt will now show `(venv)` to indicate the active environment.)*

5. Run `pip install -r requirements.txt`.
6. Ensure the virtual environment is still active, then execute: `python3 main.py`
7. Follow directions as prompted.
8. **Deactivate the Virtual Environment (When Finished)** `deactivate`