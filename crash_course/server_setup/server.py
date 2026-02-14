from mcp.server.fastmcp import FastMCP
import os
import platform
from datetime import datetime

# Create MCP server
mcp = FastMCP("my-first-server")


# Tool 1
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b


# Tool 2
@mcp.tool()
def read_file(path: str) -> str:
    """Read file contents"""
    if not os.path.exists(path):
        return "File not found"
    
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# Tool 3
@mcp.tool()
def system_info() -> dict:
    """Get system info"""
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "cpu": platform.processor(),
        "time": datetime.now().isoformat()
    }


# CRITICAL FIX: explicit stdio transport
if __name__ == "__main__":
    mcp.run(transport="stdio")