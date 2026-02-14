import asyncio
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession


async def main():

    # Correct way: define server parameters
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    # Connect to MCP server
    async with stdio_client(server_params) as streams:

        async with ClientSession(*streams) as session:

            # List available tools
            tools = await session.list_tools()

            print("\nAvailable tools:")
            for tool in tools.tools:
                print("-", tool.name)

            # Call add tool
            result = await session.call_tool(
                "add",
                {"a": 5, "b": 7}
            )

            print("\nAdd result:", result.content)


asyncio.run(main())