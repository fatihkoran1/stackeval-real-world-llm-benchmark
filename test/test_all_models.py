import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

# Load env
load_dotenv()

# Clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# 🔥 PROMPT BUILDER 
def build_prompt(user_question):
    return f"""
You are answering a real Stack Overflow style C programming question.

{user_question}

Please:
1. Explain the problem
2. Identify what is wrong
3. Provide a correct solution
4. Show the corrected code

Keep the answer focused and practical.
Avoid repetition and unnecessary background details.
Provide one clear fix and corrected code.
"""

# ONLY CHANGE THIS PART
raw_question = """
Question:
Why is my string not changing after passing it to a function in C?

Code:
#include <stdio.h>

void changeString(char str[]) {
    str = "Hello";
}

int main() {
    char str[] = "World";
    changeString(str);
    printf("%s", str);
    return 0;
}

"""

question = build_prompt(raw_question)

# Models
models = [
    {"label": "Frontier proprietary model", "provider": "openai", "model_name": "gpt-5.4"},
    {"label": "Frontier competitor", "provider": "anthropic", "model_name": "claude-sonnet-4-6"},
    {"label": "Open-source model", "provider": "openrouter", "model_name": "meta-llama/llama-4-maverick"},
    {"label": "Budget / lightweight model", "provider": "openai", "model_name": "gpt-5.4-mini"}
]

json_filename = "all_model_results.json"
txt_filename = "all_model_results_readable.txt"

results = []

for item in models:
    label = item["label"]
    provider = item["provider"]
    model_name = item["model_name"]

    print(f"\n===== {label} =====")
    print(f"Model: {model_name}\n")

    try:
        if provider == "openai":
            response = openai_client.responses.create(
                model=model_name,
                input=question
            )
            answer_text = response.output_text

        elif provider == "anthropic":
            response = anthropic_client.messages.create(
                model=model_name,
                max_tokens=1000,
                messages=[{"role": "user", "content": question}]
            )
            answer_text = response.content[0].text

        elif provider == "openrouter":
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {openrouter_api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model_name,
                    "messages": [{"role": "user", "content": question}]
                },
                timeout=60
            )
            response.raise_for_status()
            answer_text = response.json()["choices"][0]["message"]["content"]

        else:
            answer_text = f"ERROR: Unsupported provider: {provider}"

    except Exception as error:
        answer_text = f"ERROR: {str(error)}"

    print(answer_text)
    print("\n" + "=" * 50)

    results.append({
        "label": label,
        "provider": provider,
        "model": model_name,
        "question": raw_question.strip(),
        "answer": answer_text
    })

# JSON
existing_results = []

if os.path.exists(json_filename):
    try:
        with open(json_filename, "r", encoding="utf-8") as f:
            existing_results = json.load(f)
    except:
        existing_results = []

existing_results.extend(results)

with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(existing_results, f, indent=4, ensure_ascii=False)

# TXT: append 
with open(txt_filename, "a", encoding="utf-8") as f:
    f.write(f"\nQuestion:\n{raw_question.strip()}\n\n")

    for r in results:
        f.write(f"===== {r['label']} =====\n")
        f.write(f"Model: {r['model']}\n\n")
        f.write(r["answer"])
        f.write("\n\n" + "=" * 70 + "\n\n")

print("\nSaved / updated files:")
print(f"- {json_filename}")
print(f"- {txt_filename}")