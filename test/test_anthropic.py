import os
import json
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env
load_dotenv()

# Create Anthropic client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Test question
question = "Why do I get a NullPointerException in Java?"

# Send request to Claude Sonnet 4.6
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=800,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

# Get clean answer text
answer_text = response.content[0].text

# Build result object for JSON storage
result = {
    "question": question,
    "model": "claude-sonnet-4-6",
    "answer": answer_text
}

# Save machine-readable result
with open("anthropic_test_result.json", "w", encoding="utf-8") as json_file:
    json.dump(result, json_file, indent=4, ensure_ascii=False)

# Save human-readable result
with open("anthropic_readable.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(f"Question:\n{question}\n\n")
    txt_file.write("Model:\n")
    txt_file.write("claude-sonnet-4-6\n\n")
    txt_file.write("Answer:\n")
    txt_file.write(answer_text)

# Also print readable output in terminal
print("\n=== MODEL OUTPUT ===\n")
print(f"Question:\n{question}\n")
print("Model:")
print("claude-sonnet-4-6\n")
print("Answer:")
print(answer_text)
print("\n====================\n")

print("Saved files:")
print("- anthropic_test_result.json")
print("- anthropic_readable.txt")