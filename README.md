# Zero-Shot & Few-Shot Data Extraction

## Project Overview

This project demonstrates how Large Language Models (LLMs) can extract structured information from messy, unstructured text using Prompt Engineering techniques.

The solution applies delimiter-based prompts, few-shot learning, and deterministic output generation to convert natural language into structured JSON.

---

## Features

- Zero-Shot Prompting
- Few-Shot Prompting
- Strict JSON Output
- Delimiter-Based Prompting
- Temperature = 0
- Missing values handled as null

---

## Technologies

- Python 3
- OpenAI API
- Prompt Engineering

---

## Project Structure

```
project1-prompt-engineering-data-extraction/
│
├── README.md
├── LICENSE
├── requirements.txt
├── prompt.txt
├── main.py
├── sample_input.txt
├── sample_output.json
├── examples/
├── screenshots/
└── docs/
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## Sample Input

```text
Hi,

My name is Muhammad Uzair.

I am 19 years old.

Living in Wah Cantt.

Phone:
03121234567

Email:
uzair0179@gmail.com

Electrical Engineering Student.
```

---

## Sample Output

```json
{
    "name":"Muhammad Uzair",
    "age":19,
    "email":"uzair0179@gmail.com",
    "phone":"03121234567",
    "city":"Wah Cantt",
    "occupation":"Electrical Engineering Student"
}
```

---

## Future Improvements

- CSV Export
- Resume Parsing
- Invoice Extraction
- PDF Processing

---

## Author

Muhammad Uzair
