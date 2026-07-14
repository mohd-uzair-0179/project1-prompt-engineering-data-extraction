# 🚀 Zero-Shot & Few-Shot Data Extraction

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)
![Prompt Engineering](https://img.shields.io/badge/Prompt-Engineering-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> A Prompt Engineering project that transforms messy, unstructured text into clean, structured JSON using deterministic prompting, delimiters, and Few-Shot Learning.

---

## 📌 Project Overview

This project demonstrates how Large Language Models (LLMs) can reliably extract structured information from unstructured natural language.

Instead of relying on traditional parsing techniques, this project uses carefully engineered prompts to produce deterministic JSON outputs suitable for databases, APIs, and automation pipelines.

---

## ✨ Features

- ✅ Zero-Shot Prompting
- ✅ Few-Shot Prompting
- ✅ Delimiter-Based Prompt Design
- ✅ Deterministic Output (Temperature = 0)
- ✅ Strict JSON Validation
- ✅ Missing Value Handling
- ✅ Production-Ready Prompt Structure

---

## 🛠 Technologies Used

- Python 3
- OpenAI API
- Prompt Engineering
- JSON

---

## 📂 Project Structure

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
│
├── examples/
│   ├── example1.txt
│   ├── example2.txt
│   ├── output1.json
│   └── output2.json
│
├── screenshots/
│   └── README.md
│
└── docs/
    └── README.md
```

---

## ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/mohd-uzair-0179/project1-prompt-engineering-data-extraction.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the program

```bash
python main.py
```

---

## 📄 Sample Input

```text
Hello,

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

## 📄 Sample Output

```json
{
  "name": "Muhammad Uzair",
  "age": 19,
  "email": "uzair0179@gmail.com",
  "phone": "03121234567",
  "city": "Wah Cantt",
  "occupation": "Electrical Engineering Student"
}
```

---

## 📈 Future Improvements

- Resume Parsing
- Invoice Information Extraction
- CSV Export
- PDF Processing
- Batch Processing
- REST API Integration

---

## 👨‍💻 Author

**Muhammad Uzair**

Electrical Engineering Student | AI & Robotics Enthusiast

---

## 📜 License

This project is licensed under the MIT License.
