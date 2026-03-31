import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

question = "Why do I get a NullPointerException in Java?"
model_name = "meta-llama/llama-4-maverick"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": model_name,
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
response.raise_for_status()

result_json = response.json()
answer_text = result_json["choices"][0]["message"]["content"]

result = {
    "question": question,
    "model": model_name,
    "answer": answer_text
}

with open("openrouter_test_result.json", "w", encoding="utf-8") as json_file:
    json.dump(result, json_file, indent=4, ensure_ascii=False)

with open("openrouter_readable.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(f"Question:\n{question}\n\n")
    txt_file.write("Model:\n")
    txt_file.write(f"{model_name}\n\n")
    txt_file.write("Answer:\n")
    txt_file.write(answer_text)

print("\n=== MODEL OUTPUT ===\n")
print(f"Question:\n{question}\n")
print("Model:")
print(f"{model_name}\n")
print("Answer:")
print(answer_text)
print("\n====================\n")

print("Saved files:")
print("- openrouter_test_result.json")
print("- openrouter_readable.txt")