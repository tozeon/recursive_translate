# LLM Recursive Translator

## Description

This is an small python application that recursively translates text.

## How it works

It uses translategemma to translate text multiple times and outputs it into `output.txt`

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