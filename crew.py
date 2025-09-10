from crewai import Crew,Process
from task import research_task , write_task
from agents import NewsResearcher, NewsWriter

# formating the tech-focused crew with some enhanced confiuration
crew=Crew(
    agents=[NewsResearcher, NewsWriter],
    tasks=[research_task,write_task],
    process=Process.sequential,  # sequential execution to ensure tasks are completed in order
)

## satrtingg the task execution process with enchamced feedback
result=crew.kickoff(inputs={'topic': 'Artificial Intelligence in healthcare'})
print(result)