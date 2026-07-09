"""
KOKI Tool Executor
Week 4

Executes tools using the registry.
"""

from brain.tool_registry import TOOLS


def execute_tool(tool_name, argument):

    if tool_name not in TOOLS:
        return None

    try:
        return TOOLS[tool_name](argument)

    except Exception as e:
        return f"Tool Error: {e}"