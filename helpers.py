"""Helper module to aid in the usual api functions"""
import random

def get_programming_joke() -> str:
    with open('data/jokes.txt', 'r') as f:
        jokes = f.readlines()

    return random.choice(jokes)

def kill(user_name : str, your_name : str):
    with open('data/kills.txt', 'r') as f:
        responses = f.readlines()

    choice = random.choice(responses).format(your_name, user_name).strip('\n')
    return choice

def eightball(*, question : str):
    with open('data/eightball.txt', 'r') as f:
        responses = f.readlines()

    return random.choice(responses)

def get_pickup_line():
    with open('data/pickup_lines.txt', 'r') as pl:
        lines = pl.readlines()

    return random.choice(lines).strip('\n')
