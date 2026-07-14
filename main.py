"""
Project: Zero-Shot & Few-Shot Data Extraction
Author: Muhammad Uzair
Repository:
https://github.com/mohd-uzair-0179/project1-prompt-engineering-data-extraction

Description:
Reads unstructured text, sends it to an LLM using an engineered prompt,
and extracts structured information in JSON format.
"""

import json
import os
from openai import OpenAI


PROMPT_FILE = "prompt.txt"
INPUT_FILE = "sample_input.txt"
OUTPUT_FILE = "sample_output.json"


def read_file(path):
    """Read text from a file."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        exit()


def save_json(data, path):
    """Save dictionary as formatted JSON."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OpenAI API key not found.")
        print("Set OPENAI_API_KEY as an environment variable.")
        return

    client = OpenAI(api_key=api_key)

    prompt_template = read_file(PROMPT_FILE)
    raw_text = read_file(INPUT_FILE)

    prompt = prompt_template.replace(
        "{{RAW_TEXT}}",
        raw_text
    )

    try:

        response = client.chat.completions.create(
            model="gpt-4.1",
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        output = response.choices[0].message.content

        parsed = json.loads(output)

        save_json(parsed, OUTPUT_FILE)

        print("\nExtraction Successful!\n")
        print(json.dumps(parsed, indent=4))

        print(f"\nOutput saved to {OUTPUT_FILE}")

    except json.JSONDecodeError:
        print("The model returned invalid JSON.")

    except Exception as error:
        print("Error:")
        print(error)


if __name__ == "__main__":
    main()
