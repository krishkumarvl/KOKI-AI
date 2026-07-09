"""
KOKI Calculator Tool
Week 4
"""

import math


def calculate(expression):

    expression = expression.lower().strip()

    try:
        allowed = {
            "__builtins__": None,
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round,
        }

        result = eval(expression, allowed)

        return f"The answer is {result}"

    except Exception:
        return "Sorry, I couldn't calculate that."