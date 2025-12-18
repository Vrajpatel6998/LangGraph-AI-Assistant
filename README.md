# 🧠 LangGraph AI Assistant (Gemini API)

A **LangGraph-powered AI assistant** that accepts a user-defined problem and generates a **structured, step-by-step solution** using a **multi-node AI workflow**.  
This project focuses on **clean architecture, state management, and explainable AI outputs**.

---

## 📌 Overview

The LangGraph AI Assistant demonstrates how complex reasoning tasks can be broken into **independent workflow nodes**, allowing better transparency and control over AI-generated responses.

The assistant:
- Takes a problem statement from the user
- Processes it through a reasoning pipeline
- Produces a clear, structured final solution

---

## ⚙️ Tech Stack

- 🐍 **Python**
- 🔗 **LangGraph**
- 🤖 **Gemini API (google.genai)**
- 🌐 **Streamlit**

---

## 🔄 Workflow Design

The application uses a **three-node LangGraph workflow**:

### 1️⃣ Input Node
- Accepts user input
- Validates the problem statement
- Ensures clean and meaningful input

### 2️⃣ Reasoning Node
- Uses the **Gemini API**
- Generates step-by-step reasoning
- Maintains context using shared state

### 3️⃣ Final Output Node
- Produces a concise and structured solution
- Removes unnecessary reasoning noise
- Presents a clean final answer

🧩 **State is passed between nodes** to preserve context and ensure explainability.

---

## 🖥️ User Interface

Built using **Streamlit**, the UI provides:

- ✍️ Text area to enter the problem statement
- 🧠 Display of intermediate reasoning steps
- ✅ Final structured solution output

---

## 🚀 Features

- Multi-node AI reasoning workflow
- Explainable AI outputs
- Modular and scalable architecture
- Easy-to-use Streamlit interface
- Gemini API integration

---

## 📂 Project Structure

```text
langgraph-ai-assistant/
│
├── app.py                  # Streamlit / Gradio UI
├── graph/
│   ├── graph_builder.py    # LangGraph definition
│   ├── nodes.py            # Input, Reasoning, Final nodes
│   └── state.py            # Shared state definition
│
├── llm/
│   └── gemini_llm.py       # Gemini LLM config
│
├── utils/
│   └── validators.py      # Input validation
│
├── requirements.txt
├── .env
└── README.md
