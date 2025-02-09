#!/usr/bin/env python
import sys

from crew import Learn02
from datetime import datetime


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'openai',
        'date': datetime.now().strftime("%Y-%m-%d")
    }

    Learn02().crew().kickoff(inputs=inputs)

run()
