# News Reporter AI Agent

Automate technology news research and writing using CrewAI and Gemini. Two agents—a Senior Researcher and a Writer—collaborate to produce insightful, well-researched articles.

## Features

- **Automated Research:** Uses Serper API for internet search and Gemini for generative AI.
- **Collaborative Agents:** Senior Researcher uncovers trends; Writer crafts engaging articles.
- **Markdown Output:** Articles are saved in markdown format.

## Project Structure

```
News Reporter AI Agent/
│
├── Agent_crew_gemini/
│   ├── agents.py      # Defines news_researcher and news_writer agents
│   ├── crew.py        # Sets up and runs the Crew workflow
│   ├── task.py        # Specifies research and writing tasks
│   ├── tools.py       # Loads API keys and initializes SerperDevTool
│   └── __pycache__/
│
├── .env               # Stores API keys (GOOGLE_API_KEY, SERPER_API_KEY)
├── requirements.txt   # Python dependencies
```

## Setup

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Configure API keys:**
    - Add your `GOOGLE_API_KEY` and `SERPER_API_KEY` to the `.env` file.

3. **Run the crew:**
    ```sh
    python Agent_crew_gemini/crew.py
    ```

## Output

- The generated article will be saved as `new-blog-post.md` in the project directory.

## Requirements

See [`requirements.txt`](requirements.txt) for details.

## Notes

- Agents and tasks are defined in `Agent_crew_gemini/agents.py` and `Agent_crew_gemini/task.py`.
- The workflow is orchestrated in `Agent_crew_gemini/crew.py`.
- Internet search capability is provided by SerperDevTool in `Agent_crew_gemini/tools.py`.

## License

MIT License.
