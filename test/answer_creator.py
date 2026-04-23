import os
import re
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

# Files
questions_filename = "questions.txt"
json_filename = "all_model_results.json"

# Prompt builder
def build_prompt(user_question):
    return f"""
You are answering a real Stack Overflow style programming question.

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

# Models
models = [
    {"label": "Frontier proprietary model", "provider": "openai", "model_name": "gpt-5.4"},
    {"label": "Frontier competitor", "provider": "anthropic", "model_name": "claude-sonnet-4-6"},
    {"label": "Open-source model", "provider": "openrouter", "model_name": "meta-llama/llama-4-maverick"},
    {"label": "Budget / lightweight model", "provider": "openai", "model_name": "gpt-5.4-mini"}
]

def load_questions_from_txt(filename):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    questions = re.findall(r'"""(.*?)"""', content, re.DOTALL)
    cleaned_questions = [q.strip() for q in questions if q.strip()]

    return cleaned_questions

def load_existing_results(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def question_exists(existing_results, question_text):
    return any(item.get("question", "").strip() == question_text.strip() for item in existing_results)

def ask_model(provider, model_name, question):
    try:
        if provider == "openai":
            response = openai_client.responses.create(
                model=model_name,
                input=question
            )
            return response.output_text

        elif provider == "anthropic":
            response = anthropic_client.messages.create(
                model=model_name,
                max_tokens=1000,
                messages=[{"role": "user", "content": question}]
            )
            return response.content[0].text

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
            return response.json()["choices"][0]["message"]["content"]

        else:
            return f"ERROR: Unsupported provider: {provider}"

    except Exception as error:
        return f"ERROR: {str(error)}"

def main():
    all_questions = load_questions_from_txt(questions_filename)

    if not all_questions:
        print("No questions found.")
        return

    selected_questions = all_questions[:30]
    existing_results = load_existing_results(json_filename)
    new_results = []

    for index, raw_question in enumerate(selected_questions, start=1):
        print(f"\n########## QUESTION {index} ##########\n")

        if question_exists(existing_results, raw_question):
            print("This question already exists. Skipping...\n")
            continue

        question = build_prompt(raw_question)

        for item in models:
            label = item["label"]
            provider = item["provider"]
            model_name = item["model_name"]

            print(f"\n===== {label} =====")
            print(f"Model: {model_name}\n")

            answer_text = ask_model(provider, model_name, question)

            print(answer_text)
            print("\n" + "=" * 50)

            new_results.append({
                "label": label,
                "provider": provider,
                "model": model_name,
                "question": raw_question.strip(),
                "answer": answer_text
            })

    if new_results:
        existing_results.extend(new_results)

        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(existing_results, f, indent=4, ensure_ascii=False)

        print("\nSaved / updated file:")
        print(f"- {json_filename}")
    else:
        print("\nNo new results were added.")

if __name__ == "__main__":
    main()