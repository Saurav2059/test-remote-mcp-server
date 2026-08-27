from fastmcp import FastMCP
import random

mcp = FastMCP("Remote Calculator Server")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a random number."""
    return random.randint(min_val, max_val)


@mcp.tool
def ss(text: str) -> str:
    """Return the given text."""
    return text


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )