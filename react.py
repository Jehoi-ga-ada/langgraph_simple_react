from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def triple(num: float) -> float:
    """
    Triples the input number

    Args:
        num (float): a number to triple

    Returns:
        float: the triple of the input number
    """

    return float(num) * 3


tools = [TavilySearch(max_results=1), triple]

llm = ChatOllama(model="qwen3:1.7b", temperature=0).bind_tools(tools=tools)
