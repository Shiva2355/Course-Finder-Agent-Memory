# 🎓 Course Finder Agent with Memory

An AI-powered Course Finder Agent built with **LangChain, LangGraph, Groq, Tavily, and YouTube Data API**.

The agent helps students find learning roadmaps and beginner-friendly video courses based on their learning goals. It also uses **short-term memory** to remember previous conversations within the same session.

## 🚀 Features

* 🤖 AI Agent powered by Groq
* 🔎 Web research using Tavily
* 🎥 YouTube course search using YouTube Data API
* 🧠 Short-term conversational memory
* 🛠️ Custom LangChain tools
* 📚 Learning roadmap generation
* 🔗 Finds free YouTube courses and tutorials
* 💬 Remembers previous conversation in the same thread

## 🏗️ Architecture

```text
                 User
                  │
                  ▼
           LangChain Agent
                  │
          ┌───────┴────────┐
          │                │
          ▼                ▼
       Tavily          YouTube API
     Web Research      Course Search
          │                │
          └───────┬────────┘
                  ▼
              Groq LLM
                  │
                  ▼
             Final Answer
                  │
                  ▼
          LangGraph Memory
```

## 🧰 Tech Stack

* Python
* LangChain
* LangGraph
* Groq
* Tavily
* YouTube Data API
* python-dotenv
* Requests

## 📁 Project Structure

```text
course-finder-agent-memory/
│
├── app.py
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/course-finder-agent-memory.git
cd course-finder-agent-memory
```

Install dependencies:

```bash
pip install -U langchain langgraph langchain-groq langchain-tavily python-dotenv requests
```

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

Never commit your `.env` file.

Add it to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

## 🔧 How It Works

### 1. Groq LLM

The agent uses a Groq-hosted LLM as its reasoning engine.

```python
model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    api_key=google_api_key
)
```

### 2. Tavily Research Tool

Tavily is used to research:

* Learning roadmaps
* Prerequisites
* Free resources
* Certifications
* Learning recommendations

```python
course_research_tool = TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=tavily_api_key
)
```

### 3. YouTube Course Search

A custom LangChain tool searches YouTube for long-form beginner-friendly courses.

```python
@tool
def search_courses(skill: str) -> list:
    """Search for free video courses and tutorials on YouTube."""
```

The tool uses the YouTube Data API to retrieve:

* Course title
* Channel
* Published date
* Description
* YouTube link

### 4. Short-Term Memory

The project uses LangGraph's `InMemorySaver` for short-term conversation memory.

```python
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
```

A `thread_id` identifies the conversation:

```python
config = {
    "configurable": {
        "thread_id": "user-1"
    }
}
```

Because the same `thread_id` is used, the agent can access previous messages in that conversation.

## 🧠 Example

First request:

```text
I want to learn Machine Learning from scratch.
Show me the best roadmap and beginner-friendly courses.
```

The agent researches the topic and finds YouTube courses.

Then the user can ask:

```text
Suggest the best beginner course from the videos you showed.
```

Because the same conversation thread is used, the agent can refer to the previously retrieved courses.

## ▶️ Running the Project

Run:

```bash
python app.py
```

Example interaction:

```text
User:
I want to learn Machine Learning from scratch.

Agent:
Learning Roadmap
...

Video Courses
...

User:
Suggest the best beginner course from the videos you showed.

Agent:
Based on the courses shown earlier, ...
```

## 🧠 Memory Flow

```text
User Query 1
     ↓
Agent
     ↓
Tools
     ↓
Response
     ↓
Memory
     │
     ▼
User Query 2
     ↓
Same thread_id
     ↓
Agent accesses previous conversation
     ↓
Context-aware response
```

## 🔐 Security

API keys are stored in environment variables and should never be committed to GitHub.

Make sure `.gitignore` contains:

```gitignore
.env
```

If an API key is accidentally pushed to GitHub, revoke it immediately and generate a new key.

## 📌 Future Improvements

* Add a web UI using Streamlit or React
* Add persistent database-backed memory
* Add course rating and ranking
* Add course duration filtering
* Add difficulty-level filtering
* Add personalized learning plans
* Add multiple course sources
* Add user authentication
* Store user learning preferences

## 👨‍💻 Author

**Shiva**

Built as an Agentic AI project using LangChain and LangGraph.

## ⭐ If you find this project useful

Give the repository a ⭐ and feel free to explore or improve the project.
