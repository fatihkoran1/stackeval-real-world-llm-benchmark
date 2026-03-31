from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Test question
question = "Why do I get a NullPointerException in Java?"

# Send request to model
response = client.responses.create(
    model="gpt-5.4",
    input=question
)

# Get clean answer text
answer_text = response.output_text

# Build result object for JSON storage
result = {
    "question": question,
    "model": "gpt-5.4",
    "answer": answer_text
}

# Save machine-readable result
with open("openai_test_result.json", "w", encoding="utf-8") as json_file:
    json.dump(result, json_file, indent=4, ensure_ascii=False)

# Save human-readable result
with open("openai_readable.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(f"Question:\n{question}\n\n")
    txt_file.write("Model:\n")
    txt_file.write("gpt-5.4\n\n")
    txt_file.write("Answer:\n")
    txt_file.write(answer_text)

# Also print readable output in terminal
print("\n=== MODEL OUTPUT ===\n")
print(f"Question:\n{question}\n")
print("Model:")
print("gpt-5.4\n")
print("Answer:")
print(answer_text)
print("\n====================\n")

print("Saved files:")
print("- openai_test_result.json")
print("- openai_readable.txt")