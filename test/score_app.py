import json
import os
import re
from datetime import datetime

import pandas as pd
import streamlit as st

RESULTS_FILE = "all_model_results.json"
OUTPUT_FILE = "human_scores.xlsx"

st.set_page_config(page_title="LLM Scoring Form", layout="wide")
st.title("LLM Scoring Form")

st.markdown("""
### Scoring Rubric
- **0** = completely wrong or unhelpful
- **1** = partially correct but missing crucial details
- **2** = mostly correct and useful
- **3** = excellent answer I would trust completely
""")

scorer_name = st.text_input("Developer name")


def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def group_by_question(results):
    grouped = {}
    for item in results:
        question = item["question"].strip()
        if question not in grouped:
            grouped[question] = []
        grouped[question].append(item)
    return grouped


def save_to_excel(rows):
    new_df = pd.DataFrame(rows)

    if os.path.exists(OUTPUT_FILE):
        existing_df = pd.read_excel(OUTPUT_FILE)
        final_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        final_df = new_df

    final_df.to_excel(OUTPUT_FILE, index=False)


def normalize_headings(text):
    lines = text.splitlines()
    normalized_lines = []

    for line in lines:
        stripped = line.lstrip()

        if stripped.startswith("### "):
            normalized_lines.append("##### " + stripped[4:])
        elif stripped.startswith("## "):
            normalized_lines.append("##### " + stripped[3:])
        elif stripped.startswith("# "):
            normalized_lines.append("##### " + stripped[2:])
        else:
            normalized_lines.append(line)

    return "\n".join(normalized_lines)


def render_answer(answer_text):
    answer_text = normalize_headings(answer_text)

    parts = re.split(r"```(\w+)?\n(.*?)```", answer_text, flags=re.DOTALL)

    i = 0
    while i < len(parts):
        if i == 0:
            if parts[i].strip():
                st.markdown(parts[i].strip())
            i += 1
        else:
            language = parts[i] if parts[i] else "text"
            code = parts[i + 1] if i + 1 < len(parts) else ""
            st.code(code.strip(), language=language)

            if i + 2 < len(parts) and parts[i + 2].strip():
                st.markdown(parts[i + 2].strip())

            i += 3


results = load_results()

if not results:
    st.error("all_model_results.json file not found or empty.")
    st.stop()

grouped_results = group_by_question(results)

with st.form("scoring_form"):
    all_rows = []

    for question_index, (question, answers) in enumerate(grouped_results.items(), start=1):
        st.markdown(f"## Question {question_index}")
        st.code(question, language="text")

        answer_labels = ["Answer A", "Answer B", "Answer C", "Answer D"]

        for answer_index, item in enumerate(answers):
            if answer_index >= 4:
                break

            label = answer_labels[answer_index]
            st.markdown(f"### {label}")

            with st.container():
                render_answer(item["answer"])

            st.radio(
                f"Score for {label} - Question {question_index}",
                options=[0, 1, 2, 3],
                horizontal=True,
                key=f"score_{question_index}_{answer_index}"
            )

            all_rows.append({
                "question_number": question_index,
                "question": question,
                "answer_label": label,
                "model_label": item.get("label", ""),
                "provider": item.get("provider", ""),
                "model": item.get("model", ""),
                "answer": item.get("answer", ""),
                "score_key": f"score_{question_index}_{answer_index}"
            })

        st.divider()

    submitted = st.form_submit_button("Submit Scores")

if submitted:
    if not scorer_name.strip():
        st.error("Please enter developer name.")
        st.stop()

    date = datetime.now().isoformat(timespec="seconds")
    rows_to_save = []

    for row in all_rows:
        saved_row = {
            "scorer_name": scorer_name.strip(),
            "date": date,
            "question_number": row["question_number"],
            "question": row["question"],
            "answer_label": row["answer_label"],
            "model_label": row["model_label"],
            "provider": row["provider"],
            "model": row["model"],
            "answer": row["answer"],
            "score": st.session_state[row["score_key"]]
        }
        rows_to_save.append(saved_row)

    save_to_excel(rows_to_save)
    st.success(f"Scores saved to {OUTPUT_FILE}")