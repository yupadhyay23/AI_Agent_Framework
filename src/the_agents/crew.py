from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class TheAgents():
    """TheAgents crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def routing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['routing_agent'], # type: ignore[index]
            verbose=True
        )

    
    
    @agent
    def hr_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['hr_agent'], # type: ignore[index]
            verbose=False
        )

    @agent
    def finance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['finance_agent'], # type: ignore[index]
            verbose=False
        )
        
    @agent
    def email_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_agent'], # type: ignore[index]
            verbose=False
        )
        
    @agent
    def web_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['web_search_agent'], # type: ignore[index]
            verbose=False
        )        

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    
    @task
    def routing_task(self) -> Task:
        return Task(
            config=self.tasks_config['routing_task'] # type: ignore[index]  
        )
    
    @task
    def hr_task(self) -> Task:
        return Task(
            config=self.tasks_config['hr_task'], # type: ignore[index]
            output_file='report.md'
        )

    @task
    def finance_task(self) -> Task:
        return Task(
            config=self.tasks_config['finance_task'], # type: ignore[index]
            output_file='report.md'
        )
        
    @task
    def email_task(self) -> Task:
        return Task(
            config=self.tasks_config['email_task'], # type: ignore[index]
            output_file='report.md'
        )
        
    @task
    def web_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['web_search_task'], # type: ignore[index]
            output_file='report.md'
        )        

    @crew
    def crew(self) -> Crew:
        """Creates the TheAgents crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
