from crewai import Agent, Task, Crew, Process

# Define agents
researcher = Agent(
    role="Researcher",
    goal="Provide guidance and advice on computer science and data science topics",
    backstory="You're an expert researcher specializing in AI technology.",
    allow_delegation=False
)

writer = Agent(
    role="Senior Writer",
    goal="Create compelling content about AI and AI agents",
    backstory="You're a senior writer specializing in technology and AI topics.",
    allow_delegation=False
)

# Define task
task = Task(
    description="Generate 5 interesting ideas for an article about AI agents, then write a captivating paragraph for each idea.",
    expected_output="5 bullet points, each with a paragraph showcasing the potential of a full article on the topic."
)

# Create the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[task],
    process=Process.hierarchical
)

# Run the crew
result = crew.kickoff()

print(result)
