def regularize_output(response):
    """
    This function regularizes the response based on certain conditions, such as penalizing
    responses that are too short or too long. You can add more conditions as needed.

    Args:
    - response (str): The generated response from the model.

    Returns:
    - str: The regularized response.
    """

    # Define some thresholds
    MIN_LENGTH_THRESHOLD = 10  # You can adjust this as per your requirements
    MAX_LENGTH_THRESHOLD = 250  # Adjust this based on the maximum length you desire

    # Check if the response is too short
    if len(response) < MIN_LENGTH_THRESHOLD:
        return "I'm sorry, I couldn't generate a detailed response. Can you provide more context or rephrase?"

    # Check if the response is too long
    if len(response) > MAX_LENGTH_THRESHOLD:
        response = response[:MAX_LENGTH_THRESHOLD]  # Truncate the response
        response += "..."  # Add ellipsis to indicate truncation

    return response
