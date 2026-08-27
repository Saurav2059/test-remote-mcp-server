from fastmcp import FastMCP
import random
import json


# Create MCP server
mcp = FastMCP("Simple Calculator Server")


# --------------------------------------------------
# Tool 1: Add two numbers
# --------------------------------------------------

@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers and return the result.
    """
    return a + b


# --------------------------------------------------
# Tool 2: Generate random number
# --------------------------------------------------

@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """
    Generate a random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)


# --------------------------------------------------
# Resource: Server information
# --------------------------------------------------

@mcp.resource("info://server")
def server_info() -> str:
    """
    Get information about this MCP server.
    """

    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with calculator tools",
        "tools": [
            "add",
            "random_number"
        ],
        "transport": "HTTP",
        "author": "Your Name",
    }

    return json.dumps(info, indent=2)


# --------------------------------------------------
# Start Remote MCP Server
# --------------------------------------------------

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )