from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os

## calling the geminimodel 
llm=ChatGoogleGenerativeAI(model="gemini-2.5-pro",
                           verbose="True",
                           tempreature=0.1,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))


## creating a senio agent with memmory and verbbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Uncover the ground breaking technologies in {topic}',
    verbose=True,
    memmory=True,
    backstory=(
        "Driven by curiosity and a passion for innovation,"
        "eager to explore the frontiers of technology and uncover the next big breakthrough."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

## creating a writer agent with custom tools responsible for writing news blog

news_writer=Agent(
    role="Writer",
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memmory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate ,bringing new"
        "technologies to life for a broad audience."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False   # research work is done by senior researcher agent
)