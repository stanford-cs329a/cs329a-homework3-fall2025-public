from typing import Literal, Optional
from cs329a_hw3.utils import generate_together

MATH = [ 
    ("A random variable X has probability density function proportional to cos(x)/sqrt(x) from 1 to 2. What is the normalization constant should this be multiplied by to make this a valid PDF? Round your answer to the nearest integer.", 13),
    ("Find the real solution to x^3 = x^5 + 100. Give your answer to the nearest hundredth.", -2.59),
    ("Calculate the area of a rectangle with length 123.45 cm and width 67.89 cm, then convert the result to square inches to the nearest integer.", 1299)
]

GOOGLE = [
    ("What 2024 Beyoncé album broke streaming records with its blend of country-pop and Americana?", "Cowboy Carter"),
    ("What is the title of the next Avatar film, scheduled for release on December 19, 2025?", "Fire and Ash"),
    ("How many restaurants in San Francisco have three Michelin stars in 2025?.", "Three"),
    ("What is the name of the restaurant in Palo Alto with a Michelin star in 2025?", "Protégé"),
    ("When does Zareen's (Palo Alto) open on Saturday? Format your answer as HH:MM AM/PM", "11:00 AM"),
    
    ("What nationality is the player who won the 2025 men's Wimbledon championship?", "Italian"),
]

WEATHER = [
    ("Were there any thunderstorms in Seattle, WA at noon on June 1st, 2025?", "No"),
    ("Which city was windier on August 1, 2025: Chicago or Boston?", "Boston"),
    ("Over the first three days of August 2025, did the morning (9AM) temperature in Miami ever drop below 70 Fahrenheit?", "No"),
]

STOCK = [
    ("Did Tesla (TSLA) stock go up or down on March 5, 2025 compared to its opening price on that day?", "up"),
    ("From 4 Nov 2024 to 6 Nov 2024 inclusive (the two days around the U.S. election), what was the change in Tesla closing stock price, rounded to the nearest percent?", 19),
    ("If Tesla's closing price on Aug 27, 2025 increased by 11.2%, what would that be, to the nearest cent?", 388.76),
]

def prepare_dataset(
    max_rows: Optional[int] = None,
    debug_mode: bool = False,
    question_type: Literal["math", "google", "weather", "stock", "all"] = "all"
):
    if question_type == "math":
        dataset = MATH[:2] if debug_mode else MATH
    elif question_type == "google":
        dataset = GOOGLE[:2] if debug_mode else GOOGLE
    elif question_type == "weather":
        dataset = WEATHER[:2] if debug_mode else WEATHER
    elif question_type == "stock":
        dataset = STOCK[:2] if debug_mode else STOCK
    else:
        dataset = WEATHER[:2] + STOCK[:2] + MATH[:2] + GOOGLE[:2] if debug_mode else WEATHER + STOCK + MATH + GOOGLE

    if max_rows:
        dataset = dataset[:max_rows]

    return {"query": [item[0] for item in dataset], "answer": [item[1] for item in dataset]}


def evaluate_qa(query: str, response: str, answer: str, model: str | None = None):
    """
    Evaluate QA performance by checking if the response is correct.
    
    If model is not provided, the response will be checked using a simple word-by-word comparison.
    
    Args:
        queries (List[str]): List of query strings
        responses (List[str]): List of model response strings
        answers (List[str]): List of ground truth answer strings
        model (str | None): The model to use for evaluation (default is None)
    
    Returns: 
        bool: True if the response is correct, False otherwise
    """
    if model:
        response_message = generate_together(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. You are given a question, response, and ground truth answer. You need to check whether the response correctly answers the question, based on the ground truth answer. If it is, return 'correct'. If it is not, return 'incorrect'. Only return either 'correct' or 'incorrect', without any other text."},
                {"role": "user", "content": f"Question: {query}\nResponse: {response}\nGround Truth Answer: {answer}."}
            ]
        )
        return response_message.content.strip().lower().startswith("correct")
    else:
        answer_words = set(word.strip('.,!?()[]{}":;') for word in str(answer).lower().split())
        return all(word in str(response).lower() for word in answer_words if word)
    
    
