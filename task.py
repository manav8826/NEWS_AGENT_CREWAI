from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

## research task 
research_task = Task(
    description=("Research the latest advancements in technology related to {topic}."
    "Focus on identifying groundbreaking technologies, innovations, and trends that are shaping the future,"
    "its market opportunities, challenges, and potential impact on society."
    ),
    expected_output='A comprehensive 3 paragraph  long report on the latest AI trends.',
    tools=[tool],
    agent=news_researcher,
)
## writing task with lang model configuration
write_task= Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends,and how its impacting the industry."
        "This article should be easy to understand ,engaging,and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,  # synchronous execution to ensure the writer waits for the researcher's output
    output_file='new-blog-post.md' # file to save the article
    )