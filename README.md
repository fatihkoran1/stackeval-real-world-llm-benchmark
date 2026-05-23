# StackEval Benchmark – Real-World LLM Evaluation

## Project Overview

This project recreates a simplified version of the **StackEval benchmark**, originally created by Prosus AI researchers.  
The goal is to compare multiple Large Language Models (LLMs) on **real Stack Overflow-style programming questions** instead of only relying on academic benchmarks such as MMLU or HumanEval.

The project focuses on understanding how useful AI models actually are in real developer scenarios through **human evaluation and benchmarking**.

---

# Problem This Project Solves

Many AI benchmarks mainly measure theoretical or academic performance.  
However, models that score highly on academic tests do not always perform well when solving practical developer problems.

This project tries to solve that gap by evaluating LLMs on:
- Real debugging questions
- Real programming issues
- Real developer workflows
- Human usefulness instead of only automated metrics

The benchmark helps answer questions such as:
- Which models are actually useful for developers?
- Do expensive frontier models always perform better?
- Can smaller or cheaper models compete in certain tasks?
- How reliable are LLMs in real-world coding scenarios?

---

# What This Project Does

The system:
1. Collects real programming questions from Stack Overflow
2. Sends the same questions to multiple LLMs using APIs
3. Stores all generated answers automatically
4. Lets human developers score the responses
5. Analyzes and compares the benchmark results

The project recreates the workflow of a professional LLM benchmark on a smaller educational scale.

---

# Main Features

- Multi-model LLM benchmarking
- API-based automated querying
- Real Stack Overflow coding questions
- Human evaluation scoring system (0–3 rubric)
- Structured output storage (JSON/TXT)
- Cross-model comparison
- Cost vs quality comparison
- Benchmark result analysis
- Reproducible testing workflow

---

# Technologies Used

## Languages & Tools
- Python
- Jupyter Notebook
- JSON
- Git & GitHub

## APIs & Platforms
- OpenAI API
- Anthropic API
- OpenRouter API

## Models Used
- GPT-5.4
- GPT-5.4-mini
- Claude Sonnet 4.6
- Llama 4

## Libraries
- requests
- pandas
- python-dotenv
- streamlit

---

# Architecture / Technical Concepts

## API-Based Benchmark Pipeline

The project uses an automated API workflow instead of manual prompting.  
This improves:
- Consistency
- Reproducibility
- Scalability
- Reduced human error

Each question is automatically sent to all selected models, and outputs are saved into structured files for later evaluation.

## Human Evaluation System

Instead of relying only on automated metrics, the project uses human scoring:
- 0 = completely wrong
- 1 = partially correct
- 2 = mostly correct
- 3 = excellent/trustworthy answer

This makes the benchmark closer to real developer experience.

## Benchmark Design Concepts

- LLM evaluation
- Benchmark methodology
- Prompt consistency
- Model comparison
- Experimental design
- Cost vs performance analysis

---

# What I Personally Worked On / Learned

## What I Worked On

- Selecting and comparing LLM models
- Designing the benchmark methodology
- Building the API-based querying system
- Automating response collection
- Creating the scoring workflow
- Designing human evaluation criteria
- Testing multiple models
- Analyzing benchmark results
- Structuring benchmark datasets

## What I Learned

- How professional AI benchmarking works
- How to use multiple LLM APIs together
- Benchmark design principles
- Model evaluation strategies
- Importance of reproducibility
- Trade-offs between model quality and cost
- Human evaluation limitations and subjectivity
- Organizing AI experiments systematically

---

# Project Depth

This project became relatively deep compared to many beginner AI projects because it was not only about calling APIs.

The project includes:
- Benchmark methodology
- Human evaluation
- Experimental design
- Multi-model comparison
- API automation
- Reproducibility
- Structured scoring systems
- Analysis of real-world LLM behavior

The technical implementation itself is moderate, but the reasoning, benchmarking process, and evaluation methodology add significant depth.

---

# Project Type

- School Project ✅
- Personal Research Project ✅

This started as a GenAI university research project but also became a personal exploration into LLM benchmarking and real-world AI evaluation.

---


## Alternative Version

Designed and implemented a real-world LLM benchmarking system inspired by StackEval. Compared multiple AI models using human-scored programming tasks, automated API pipelines, and benchmark analysis to evaluate practical developer usefulness.

---

# Possible Future Improvements

- Add more programming languages
- Increase benchmark dataset size
- Add automated evaluation metrics
- Improve the Streamlit scoring interface
- Add statistical analysis dashboards
- Compare open-source vs proprietary models more deeply
- Add RAG-based benchmarking scenarios
- Add hallucination/error-type analysis
- Export results into visual leaderboards
- Add developer agreement/inter-rater reliability analysis

---

# Repository Goals

This repository is not only meant to show the final result.  
It also documents:
- The experimentation process
- Benchmark design decisions
- API implementation steps
- Evaluation methodology
- Research reasoning
- Git-based development history

The goal is to make the entire AI benchmarking process transparent and reproducible.
