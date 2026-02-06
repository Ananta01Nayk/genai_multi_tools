## GenAI Multi-Agent Tool-Calling Chatbot

This project is a production-style GenAI chatbot built using LangGraph, LangChain, and Streamlit.  
It demonstrates how Large Language Models (LLMs) can plan, execute, and verify tasks** by intelligently calling real-world APIs.

---

## 🚀 Key Highlights

-  Multi-agent GenAI architecture (Planner, Executor, Verifier)
-  LLM tool calling using LangChain `@tool`
-  Real-time Weather API (OpenWeatherMap)
-  Real-time Stock Price API (Alpha Vantage)
-  Web search fallback (DuckDuckGo)
-  Interactive Streamlit UI
-  Runs locally with **one command**
-  No hard-coded responses

---

## 🏗️ Architecture Overview

### Agent Roles

| Agent | Description |
|-----|------------|
| **Planner Agent** | Understands user intent and selects the most appropriate tool |
| **Executor Agent** | Executes the selected tool using LangGraph ToolNode |
| **Verifier Agent** | Validates tool output and generates the final user response |

### Execution Flow

```ini
User Input
   ↓
Planner Agent (decides tool usage)
   ↓
Executor Agent (calls external API)
   ↓
Verifier Agent (formats final answer)
   ↓
User Output
```

LangGraph orchestrates this flow, ensuring structured execution and reliable outputs.

---

## 🧰 Integrated Tools & APIs

### 1 Weather Tool

- **API:** OpenWeatherMap
- **Purpose:** Fetch real-time weather data (temperature, condition)

### 2 Stock Price Tool

- **API:** Alpha Vantage
- **Purpose:** Fetch real-time stock prices (e.g., Google / GOOGL)

### 3 Search Tool

- **API:** DuckDuckGo Search
- **Purpose:** General informational queries only

---

## 📁 Project Structure

```ini
ai_ops_assistant/
│
├── app.py                     # Streamlit UI
├── backend.py                 # Graph initialization
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
├── .env.example               # Environment variable template
│
├── agents/
│   ├── planner.py             # Planner Agent
│   └── verifier.py            # Verifier Agent
│
├── graph/
│   ├── builder.py             # LangGraph wiring
│   └── state.py               # Chat state definition
│
├── tools/
│   ├── tools_registry.py      # Central tool registry
│   ├── weather.py             # Weather API tool
│   ├── stock.py               # Stock price API tool
│   └── search.py              # DuckDuckGo search tool
│
└── llm/
    └── client.py              # OpenAI LLM client
```

---

## ⚙️ Local Setup Instructions

### 1 Clone Repository

```bash
git clone <your-github-repo-url>
cd ai_ops_assistant
```

---

### 2 Create Virtual Environment (Recommended)

```bash
python -m venv chat
```

Activate:

**Windows**

```bash
chat\Scripts\activate
```

**Mac / Linux**

```bash
source chat/bin/activate
```

---

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
OPENWEATHER_API_KEY=your_openweather_key
ALPHAVANTAGE_API_KEY=your_alphavantage_key
```

---

### 5 Run the Application

```bash
streamlit run app.py
```

The app will be available at:

```sh
http://localhost:8501
```

---

## 🧪 Example Prompts

```ini
What is the weather in Delhi?
What is the current stock price of Google?
What is OpenAI?
Explain today’s stock market trends
```

---

## ⚠️ Known Limitations

- Free-tier APIs may have rate limits
- Stock prices may not always be perfectly real-time
- Search is restricted to avoid unreliable numeric answers

These reflect **real-world production tradeoffs**.

---

## ✅ Assignment Compliance

-  Multi-agent design
-  LLM tool calling
-  ≥2 real third-party APIs
-  End-to-end execution
-  Local run with one command
-  Clean, explainable architecture

---

## 📌 Conclusion

This project demonstrates a **robust GenAI system** with:

- intelligent tool selection
- reduced hallucinations
- real-world API integration
- modular, scalable design
