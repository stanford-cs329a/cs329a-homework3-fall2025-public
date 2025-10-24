from pydantic import BaseModel
from typing import Dict, Any, List
from concurrent.futures import ThreadPoolExecutor
from cs329a_hw3.api_manager import APIManager
from cs329a_hw3.utils import generate_together

class SubQuery(BaseModel):
    api: str
    params: Dict
    order: int

class DecompositionResponse(BaseModel):
    sub_queries: List[SubQuery]

class MultiLMAgent:
    """A class to manage multiple language models for generation, iterative refinement, and fusion"""
    
    def __init__(
        self,
        api_manager: APIManager,
        decomposition_model: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        iterative_refinement_model: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        fusion_model: str = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        generation_temp: float = 0.7,
    ):
        """Initializes the MultiLMAgent.

        Args:
            api_manager (APIManager): An instance of APIManager for API interactions.
            decomposition_model (str): Model used for query decomposition.
            iterative_refinement_model (str): Model used for iterative refinement.
            fusion_model (str): Model used for fusing responses.
            generation_temp (float): Temperature for language model generation.
        """
        ################ CODE STARTS HERE ###############
        pass
        ################ CODE ENDS HERE ###############

    def generate(
        self, 
        query: str, 
        model: str = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature: float = 0.7
    ) -> str:
        """Generates a response to the query using the specified model."""
        # Hint: use `generate_together` function from `utils.py.
        ################ CODE STARTS HERE ###############
        pass
        ################ CODE ENDS HERE ###############
    
    def single_LM_with_single_API_call(self, query: str, model: str) -> str:
        """Generates a response by querying the API manager for the necessary data and then using an LM to generate a final response based on the API output."""
        ################ CODE STARTS HERE ###############
        pass
        ################ CODE ENDS HERE ###############

    def _get_query_decomposition_prompt(self, query: str) -> str:
        """Helper function to generate a prompt for the LLM to decompose the query into sub-queries."""
        ################ CODE STARTS HERE ###############
        # Hint: A helpful way structure the output is to enclose each sub-query in <sub-query>...</sub-query> tags. You should provide the model with instructions on how to decompose the query into sub-queries.
        pass
        ################ CODE ENDS HERE ###############s

    def _get_sub_queries(self, query: str, max_sub_queries: int = 4) -> List[str]:
        """Helper function to break down a complex user query into smaller subqueries."""
        ################ CODE STARTS HERE ###############
        # You should use an LLM to decompose the query and parse the output to return the 
        # list of (natural language) sub-queries.
        pass
        ################ CODE ENDS HERE ###############
    
    def decompose_query(self, query: str, max_sub_queries: int = 4) -> List[Dict[str, Any]]:
        """Decomposes a query into independent, more manageable sub-queries that are executed in parallel via the API manager.

        Args:
            query (str): The user's original query.
            max_sub_queries (int): The maximum number of sub-queries to generate.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, where each contains the
            sub-query, the API used to answer the sub-query, parameters, results, and any errors.
        """
        ################ CODE STARTS HERE ################
        # HINT: Route each of the natural language sub-queries to the API manager and gather the results.
        pass
        ################ CODE ENDS HERE ###############

    def _get_synthesis_prompt(self, query: str, decomposed_queries: List[Dict[str, Any]] = None) -> str:
        """
        Constructs a prompt for an LLM to synthesize a final response to the user's query, using the API results of the decomposed sub-queries.s
        """
        ################ CODE STARTS HERE ###############
        pass
        ################ CODE ENDS HERE ###############

    def decompose_and_fuse(self, query: str) -> str:
        """
        Decomposes a user query into independent sub-queries for API execution, then synthesizes the resulting outputs into a single, coherent response by prompting multiple models and fusing their generated answers.
        """
        ################ CODE STARTS HERE ###############
        # For the fusion component, you should sample responses for the synthesis prompt across
        # "google/gemma-3n-E4B-it", "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo", and
        # "OpenAI/gpt-oss-20B" and fuse them into a single coherent response.
        pass
        ################ CODE ENDS HERE ###############
    
    def _get_iterative_refinement_prompt(self, original_query: str, history: List[Dict[str, Any]]) -> str:
        """
        Helper function to generate the prompt for the iterative refinement model.
        """
        ################ CODE STARTS HERE ###############
        # HINT: As with query decomposition, a helpful way to structure the output is prompt the 
        # model to output either <sub-query>...</sub-query> or <final_answer>...</final_answer>
        # tags, and then parse the output to get the next action.
        pass
        ################ CODE ENDS HERE ###############
        

    def iterative_refine(self, query: str, max_iterations: int = 3) -> str:
        """
        Sequentially generates and executes natural language sub-queries to answer a complex query. At each step, the model can either issue a new sub-query (e.g. if additional information is needed, or if a prior sub-query failed), or return the final answer if it has enough information.
        """
        ################ CODE STARTS HERE ###############
        pass
        ################ CODE ENDS HERE ###############
        

    def run_pipeline(self, query: str) -> str:
        """
        Runs the full agentic pipeline for a given query.
        """
        ################ CODE STARTS HERE ###############
        pass
        ################ CODE ENDS HERE ###############