import requests
import json
from googleapiclient.discovery import build
from geopy.geocoders import Nominatim
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from bs4 import BeautifulSoup
import polygon
import cs329a_hw3.wolfram_api as wolfram_api
import nest_asyncio
from cs329a_hw3.utils import generate_together

# Pydantic models for structured LLM parsing
class GoogleSearchParams(BaseModel):
    search_query: str
    num_results: int = Field(default=2, description="The number of results to return from the Google search")

class StockDataParams(BaseModel):
    ticker: str = Field(description="The stock ticker symbol to get data for, e.g. 'AAPL'")
    date: str = Field(description="The date to get stock data for, in the format 'YYYY-MM-DD'")

class ComputeParams(BaseModel):
    wolfram_query: str = Field(description="The mathematical computation / operation to perform, e.g. 'integrate cos(x)/sqrt(x) from 0 to 1'")

class GetWeatherParams(BaseModel):
    location: str = Field(description="The location to get weather data for, in the format 'City, Country'")
    date: str = Field(description="The date to get weather data for, in the format 'YYYY-MM-DD'")
    hour: str = Field(default="12", description="The hour of the day to get weather data for, in the format 'HH' (24-hour format)")

class APIResponse(BaseModel):
    api_name: str = Field(description="The name of the API to use for the query. Must be one of: 'google_search', 'get_stock_data', 'compute', 'get_weather'")


class APIManager:
    """A unified class to manage various API interactions, using an LLM to route queries."""
    
    def __init__(
        self, 
        google_api_key: str, 
        google_cx_id: str, 
        polygon_api_key: str, 
        wolfram_app_id: str, 
        router_model: str = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
    ):
        """Initializes the APIManager with the necessary API keys."""
        
        with open("weather_codes.json", "r") as f:
            self._weather_codes = json.load(f)

        self.api_functions = {
            "google_search": (self.google_search, GoogleSearchParams), 
            "get_stock_data": (self.get_stock_data, StockDataParams),
            "compute": (self.compute, ComputeParams),
            "get_weather": (self.get_weather, GetWeatherParams)
        }
        ################ CODE STARTS HERE ################
        pass
        ################ CODE ENDS HERE ################

    def _parse_query_params(
        self,
        query: str, 
        function_name: str,
        model: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Uses an LLM to parse parameters for a given function from a user query.

        Args:
            query (str): The natural language user query.
            function_name (str): The name of the API function to parse parameters for.
            model (Optional[str]): The specific model to use for parsing. Defaults to the
                instance's router_model.

        Returns:
            Optional[Dict[str, Any]]: A dictionary of validated parameters, or None if
            parsing or validation fails.
        """
        ################ CODE STARTS HERE ################
        # HINT: Use the `generate_together` function with a Pydantic JSON schema 
        # (https://docs.together.ai/docs/json-mode) to parse parameters from the query. 
        # The function's docstring (e.g. `function_name.__doc__`) and the
        # Pydantic model's schema (e.g. `params_model.model_json_schema()`)
        # can be used to construct a system prompt that instructs the model to extract
        # the necessary parameters. The prompt must explicitly instruct the model to use JSON.
        # Since `generate_together` returns a `Message` object, you need to extract its content 
        # using `response_message.content`.
        
        pass
        ################ CODE ENDS HERE ################

    def route_query(self, query: str, model: Optional[str] = None) -> Dict:
        """Determines the appropriate API for a query, parses parameters, and executes the API call.

        This method first uses an LLM to decide which API tool is best suited for the
        user's query. It then calls `parse_query_params` to extract the necessary
        arguments and finally executes the chosen API function.

        Args:
            query (str): The natural language user query.
            model (Optional[str]): The specific model to use for routing. Defaults to the
                instance's router_model.

        Returns:
            Dict[str, Any]: A dictionary containing the results of the API call, the
            name of the API used, the parameters, and any potential errors.
        """
        ################ CODE STARTS HERE ################
        # HINT: Use the `APIResponse` Pydantic model to make a structured call for deciding which API to use, before parsing the query parameters for the selected API.
        pass
        ################ CODE ENDS HERE ################
        
    def _extract_webpage_content(self, url: str) -> str:
        """Helper to scrape and clean text content from a URL.

        Args:
            url (str): The URL of the webpage to scrape.

        Returns:
            str: The extracted and cleaned text content, truncated to 2000 characters.
        """
        ################ CODE STARTS HERE ################
        pass
        ################ CODE ENDS HERE ################
        
        
    def google_search(self, search_query: str, num_results: int = 2) -> List[Dict]:
        """Performs a Google search for general knowledge questions, recent events, or information not covered by other tools."""
        
        # This function should return a list of dictionaries, where each dictionary contains the title, link, snippet, and webpage content of a search result.
        # If there is an error, return a list with a dictionary containing an "error" key containing the error message.
        ################ CODE STARTS HERE ################
        # HINT: Use the Google Custom Search API to perform a Google search for the given query.
        pass
        ################ CODE ENDS HERE ################

    def get_stock_data(self, ticker: str, date: str) -> Dict[str, Any]:
        """Retrieves historical stock data (open, high, low, close, volume) for a given ticker (e.g. 'AAPL') and YYYY-MM-DD date (e.g. '2025-03-05')."""
        
        # This function should return a dictionary containing the date, open, high, low, close, and volume of the stock data.
        # If there is an error, return a dictionary with an "error" key containing the error message.
        ################ CODE STARTS HERE ################
        pass
        ################ CODE ENDS HERE ################
        
    def get_weather(self, location: str, date: str, hour: str = "12") -> Dict[str, Any]:
        """
        Fetches weather data (temperature, humidity, wind speed) for a specific location (e.g. 'Palo Alto, CA') and YYYY-MM-DD date (e.g. '2025-10-22') and HH hour (e.g. '15' for 3PM).
        """
        
        # This function should return a dictionary containing the temperature, weather description, humidity, and wind speed of the weather data.
        # If there is an error, return a dictionary with an "error" key containing the error message.
        ################ CODE STARTS HERE ################
        # HINT: Use the Nominatim geocoder to get the latitude and longitude of the location, 
        # and then use the Open Meteo API to fetch weather data for the given location, date, and hour.
        # You can translate a numerical weather code to a weather description using the `_weather_codes` dictionary.
        pass
        ################ CODE ENDS HERE ################

    def compute(self, wolfram_query: str) -> Dict[str, str]:
        """Performs a mathematical computation or operation using Wolfram Alpha."""
        
        # This function should return a dictionary containing the results of the computation.
        # If there is an error, return a dictionary with an "error" key containing the error message.
        try:
            nest_asyncio.apply()
            ################ CODE STARTS HERE ################
            # HINT: Use the `query` method of the `wolfram_api.Client` object to perform the computation.
            pass
            ################ CODE ENDS HERE ################
        except Exception as e:
            ################ CODE ENDS HERE ################    
            pass
            ################ CODE ENDS HERE ################