from fastmcp import FastMCP
import random
import json

# Create an instance of FastMCP server with the name "calculator"
mcp=FastMCP("calculator")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@mcp.tool
def generate_random_number(min_value: int=1, max_value: int=100) -> int:
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

# Define a resource to get server information
@mcp.resource("info://server")
def get_server_info()->dict:
    """Get server information as a dictionary."""
    info = {
        "name": "Calculator Server",
        "version": "1.0.0",
        "status": "running",
        "tools": ["add", "subtract", "generate_random_number"],
    }
    return info


if __name__ == "__main__":
    # Start the FastMCP server
    # Run the server on host "0.0.0.0" and port 8000
    # for remote mcp server access
    mcp.run(transport="http", host="0.0.0.0", port=8000)