from typing import TypedDict

class GraphState(TypedDict):
    user_input: str
    reasoning_steps: str
    final_output: str