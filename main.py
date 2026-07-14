from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

with open("sample_input.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

prompt = prompt.replace("{{RAW_TEXT}}", raw_text)

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

print(response.choices[0].message.content)
