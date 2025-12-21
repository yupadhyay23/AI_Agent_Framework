# Overview
Using the template provided by CrewAI, I have designed 4 agents (HR, FINANCE, EMAIL, WEB SEARCH) to return appropriate responses to user queries.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to the project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
## Running the Project
I have written ignore commands in my .gitignore file so that my OpenAI LLM API Key as well as my Serper API key are not compromised.
To succesfully run this framework, please add a .env file to your own cloned repository with the following format:

### MODEL=gpt-4o (or any other model you wish to choose)
### OPENAI_API_KEY= "YOUR API KEY HERE"
### SERPER_API_KEY="YOUR SERPER API KEY HERE
### CREWAI_TRACING_ENABLED=true

Now that the API keys have been configured, run this from the root folder of the project (the_agents):

```bash
$ crewai run
```

This command initializes the The_Agents Crew, assembling the agents and assigning them tasks as defined in the configuration.
The program will then prompt the user for input and parse this input through the LLMs.
This will return the output of the crew of agents to the terminal as well as send this output to the report.md file.

## Understanding the Crew

The crew is made up of 4 agents (HR, FINANCE, EMAIL, WEB SEARCH) all equipped with directives and specialized abilities to answer user queries.
Once the question has been parsed through the LLMs, a response will be outputted to both the terminal and report.md file. Access to google API has been
given so that the web search agent may provide the user with up to date information.

## Recent Updates Made
I have recently configured an additional agent, the Routing agent. This agent's only task is to choose the most appropriate
agent based on the user query. This wil ensure the correct approach is taken by the LLM when understanding, analyzing, and 
most importantly returning an appropriate answer back to the user.