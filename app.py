import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_tavily import TavilySearch
import json
# Load environment variables from .env file
load_dotenv()

# Step 1: Initialize the Model
google_api_key = os.getenv('GOOGLE_API_KEY')
model = init_chat_model(
    "groq:openai/gpt-oss-120b",
    api_key=google_api_key
)

# Step 2: Create Course Research Tool (Tavily)
tavily_api_key = os.getenv('TAVILY_API_KEY')
course_research_tool = TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=tavily_api_key
)

# Step 3: YouTube Course Search Tool
@tool
def search_courses(skill: str) -> list:
    """Search for free video courses and tutorials on YouTube."""
    print(f"\nCalling search_courses tool")
    print(f"Searching YouTube courses for: {skill}")
    
    youtube_api_key = os.getenv('YOUTUBE_API_KEY')
    url = "https://www.googleapis.com/youtube/v3/search"
    
    params = {
        "part": "snippet",
        "q": f"{skill} complete course tutorial",
        "type": "video",
        "videoDuration": "long",
        "maxResults": 5,
        "order": "relevance",
        "key": youtube_api_key
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    results = []
    for item in data.get("items", []):
        results.append({
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published": item["snippet"]["publishedAt"][:10],
            "description": item["snippet"]["description"][:150],
            "link": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })
    
    return json.dumps(results)
from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()


# write your code here


# Step 4: Define System Prompt
system_prompt = """You are a CourseFinder assistant that helps students discover the best learning resources.
You have access to these tools:
- course_research_tool: Research learning roadmaps, free resources, certification options, and skill prerequisites
- search_courses: Find free video courses and tutorials on YouTube
Help students by:
1. Using course_research_tool to provide a comprehensive learning roadmap
2. Using search_courses to find relevant YouTube tutorials and courses
3. Present results in clear sections: Learning Roadmap and Video Courses
Do NOT use markdown format. Use plain text with clear headings."""

# Step 5: Create and Run the Agent
agent = create_agent(
    model=model,
    tools=[course_research_tool, search_courses],
    system_prompt=system_prompt,
    checkpointer=checkpointer
)
config = {
    "configurable": {
        "thread_id": "user-1"
    }
}
user_query = "I want to learn Machine Learning from scratch. Show me the best roadmap and find me beginner-friendly courses"
response = agent.invoke({
    "messages": [{"role": "user", "content": user_query}]
},config=config)
print(response["messages"][-1].content)
user_query = "Suggest the best beginner course from the videos you showed"
response = agent.invoke({
    "messages": [{"role": "user", "content": user_query}]
},config=config)

print(response["messages"][-1].content)