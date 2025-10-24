import os
import time
import openai
from typing import List, Dict, Optional

# Global client to be initialized once
_client = None

def get_together_client():
    """Initializes and returns a reusable Together AI client."""
    global _client
    if _client is None:
        api_key = os.environ.get("TOGETHER_API_KEY")
        if not api_key:
            raise ValueError("TOGETHER_API_KEY not found in environment variables.")
        
        _client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.together.xyz/v1",
        )
    return _client

def generate_together(
    model: str,
    messages: List[Dict],
    temperature: float = 0.7,
    response_format: Optional[Dict] = None,
    max_tokens: Optional[int] = None
):
    """
    Generates a response from a model on Together AI with support for structured output.
    """
    client = get_together_client()

    args = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }
    if response_format:
        args["response_format"] = response_format
    if max_tokens:
        args["max_tokens"] = max_tokens
    for attempt in range(3):
        try:
            response = client.chat.completions.create(**args)
            return response.choices[0].message
        except Exception as e:
            print(f"API call failed on attempt {attempt + 1}: {e}")
            print(f"\tArguments: {args}")
            if attempt < 2:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                print("Final attempt failed. Returning None.")
                return None