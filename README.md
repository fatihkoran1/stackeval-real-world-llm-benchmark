# 🚀 Recreating StackEval – Real-World LLM Benchmark

## 📌 Project Overview
This project aims to recreate a simplified version of the StackEval benchmark developed by Prosus AI researchers.

Many Large Language Models (LLMs) perform similarly on academic benchmarks such as MMLU, but their performance can differ significantly when solving real developer problems.

The goal of this project is to evaluate multiple LLM models using real coding questions and human evaluation to better understand their real-world usefulness.

---

## ❗ The Core Problem
Most LLM comparisons rely on academic benchmarks such as:
- MMLU  
- HumanEval  
- GSM8K  

These benchmarks test theoretical knowledge or synthetic tasks, which do not always reflect real developer problems.

As a result, models that perform well on academic tests may still give unhelpful answers in practical situations.

This project investigates the gap between academic benchmark performance and real-world usefulness.

---

## ❓ Main Research Question
**How can we build benchmarks that better predict real-world LLM performance?**

### Sub-questions:
- Do models that perform well on academic benchmarks also perform well on real coding problems?
- Do different models specialize in different types of tasks?
- Can cheaper or smaller models perform as well as expensive models in certain scenarios?

---

## 🧠 What is StackEval?
StackEval is a benchmark created by Prosus researchers to evaluate LLMs using real developer questions.

Instead of relying only on automated metrics, StackEval uses human developers to evaluate model responses.

The goal is to measure whether the answers are actually helpful in real-world developer tasks.

---

## 🎯 Project Goal
The objective of this project is to recreate the StackEval approach on a smaller scale.

This includes:
- Collecting real coding questions  
- Generating answers from multiple LLM models  
- Having developers evaluate the answers  
- Analyzing the results  

---

## ⚙️ Methodology

### 1️⃣ Collect Real Coding Questions
- Collect 30–50 real coding questions from Stack Overflow  
- Focus on:
  - Debugging  
  - Architecture decisions  
  - Framework usage  
  - Performance issues  
- Prefer questions with accepted answers  

---

### 2️⃣ Select LLM Models
Select at least four LLM models from different categories:
- Frontier models (e.g., GPT-4)
- Competitor models (e.g., Claude)
- Open-source models (e.g., Llama)
- Budget models (e.g., Gemini Flash)

---

### 3️⃣ Generate Model Answers
- Each model answers every question  
- Example:
  - 40 questions × 4 models = 160 answers  
- Store all responses in a dataset  

---

### 4️⃣ Human Evaluation
- Recruit 2–3 software developers  
- Use a scoring rubric:

| Score | Description |
|------|------------|
| 0 | Completely wrong or useless |
| 1 | Partially correct but missing important details |
| 2 | Mostly correct and useful |
| 3 | Excellent answer that could be trusted |

---

### 5️⃣ Analyze Results
- Calculate average scores per model  
- Identify strengths and weaknesses  
- Compare performance across question types  

---

## ⚖️ Ethical Considerations
- Benchmarks influence which models are adopted  
- Human evaluation introduces subjectivity  
- Risk of models being optimized for benchmarks instead of real capability  

---

## 📊 Expected Outcome
At the end of the project, the results should include:
- A dataset of questions and model answers  
- Human evaluation scores  
- A comparison of model performance  
- Insights into real-world LLM effectiveness  

---

## 🧩 Skills Developed
This project helps develop:
- LLM evaluation skills  
- Experimental design  
- Benchmarking methodology  
- Data analysis and interpretation  

---

## 🌍 Why This Project Matters
This project demonstrates that real-world benchmarks provide more meaningful insights than generic academic benchmarks.

It helps better understand how LLMs behave in practical developer scenarios.
