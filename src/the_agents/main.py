#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from the_agents.crew import TheAgents

from contextlib import redirect_stdout
import io



warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information






# Initialize Crew
crew_instance = TheAgents().crew()
user_topic = input("Enter your query: ")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': user_topic,
        'current_year': str(datetime.now().year)
    }

    try:
        TheAgents().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")




def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": user_topic,
        'current_year': str(datetime.now().year)
    }
    try:
        TheAgents().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TheAgents().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        "topic": user_topic,
        "current_year": str(datetime.now().year)
    }

    try:
        TheAgents().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": user_topic,
        "current_year": ""
    }

    try:
        result = TheAgents().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")

