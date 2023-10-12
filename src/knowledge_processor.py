import json
import random

# Load the knowledge base
with open("config/knowledge_base.json", "r") as file:
    KNOWLEDGE_BASE = json.load(file)

USER_CONTEXT = {
    'preferences': {},
    'frequent_questions': {}
}

CURIOUS_QUESTIONS = [
    "What's your favorite movie?",
    "I've noticed you often ask about XYZ. Would you like to know more about it?",
    "How do you feel about artificial intelligence?",
    "Can you tell me more about your interests?"
]


def get_answer_from_knowledge_base(query):
    """
    Check if the query matches any predefined queries in the knowledge base and return the corresponding answer.
    Additionally, update the context based on the user's questions.

    Args:
    - query (str): The user's query.

    Returns:
    - str or None: The corresponding answer from the knowledge base, or None if no match is found.
    """
    # Update user context
    update_user_context(query)

    return KNOWLEDGE_BASE.get(query, None)


def update_user_context(query):
    """
    Updates the user's context based on the questions they ask.

    Args:
    - query (str): The user's query.
    """
    if query in USER_CONTEXT['frequent_questions']:
        USER_CONTEXT['frequent_questions'][query] += 1
    else:
        USER_CONTEXT['frequent_questions'][query] = 1


def get_curious_question():
    """
    Returns a question based on Jarviso's curiosity and what it has observed or wants to know.

    Returns:
    - str: A question.
    """
    # For simplicity, we'll use a random choice.
    # In a more advanced scenario, logic could be added to select questions based on context.
    return random.choice(CURIOUS_QUESTIONS)

# You can add more functions or logic to further process or search through the knowledge base.
