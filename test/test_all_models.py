import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

# Load API keys from .env
load_dotenv()

# Clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# One question for all models
question = "Write a function in Java that removes duplicates from a list."

# Model list
models = [
    {
        "label": "Frontier proprietary model",
        "provider": "openai",
        "model_name": "gpt-5.4"
    },
    {
        "label": "Frontier competitor",
        "provider": "anthropic",
        "model_name": "claude-sonnet-4-6"
    },
    {
        "label": "Open-source model",
        "provider": "openrouter",
        "model_name": "meta-llama/llama-4-maverick"
    },
    {
        "label": "Budget / lightweight model",
        "provider": "openai",
        "model_name": "gpt-5.4-mini"
    }
]

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
                messages=[
                    {"role": "user", "content": question}
                ]
            )
            answer_text = response.content[0].text

        elif provider == "openrouter":
            url = "https://openrouter.ai/api/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {openrouter_api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": model_name,
                "messages": [
                    {"role": "user", "content": question}
                ]
            }

            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()

            response_json = response.json()
            answer_text = response_json["choices"][0]["message"]["content"]

        else:
            answer_text = f"Unsupported provider: {provider}"

    except Exception as error:
        answer_text = f"ERROR: {str(error)}"

    print(answer_text)
    print("\n" + "=" * 50)

    results.append({
        "label": label,
        "provider": provider,
        "model": model_name,
        "question": question,
        "answer": answer_text
    })

# Save all results to one JSON file
with open("all_model_results.json", "w", encoding="utf-8") as json_file:
    json.dump(results, json_file, indent=4, ensure_ascii=False)

# Save all results to one readable TXT file
with open("all_model_results_readable.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(f"Question:\n{question}\n\n")

    for result in results:
        txt_file.write(f"===== {result['label']} =====\n")
        txt_file.write(f"Provider: {result['provider']}\n")
        txt_file.write(f"Model: {result['model']}\n\n")
        txt_file.write("Answer:\n")
        txt_file.write(result["answer"])
        txt_file.write("\n\n" + "=" * 70 + "\n\n")

print("\nSaved files:")
print("- all_model_results.json")
print("- all_model_results_readable.txt")