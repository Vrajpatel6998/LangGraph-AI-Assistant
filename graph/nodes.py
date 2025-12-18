# inputnode
def input_node(state):
    if not state["user_input"].strip():
        raise ValueError("Input cannot be empty")
    return state

# reasoning node
from llm.gemini_llm import gemini_generate

def reasoning_node(state):
    prompt = f"""
    Analyze the following problem step by step and explain your reasoning clearly.

    Problem:
    {state['user_input']}
    """
    state["reasoning_steps"] = gemini_generate(prompt)
    return state



# final output node

def final_node(state):
    prompt = f"""
    Based on the reasoning below, provide a clean, structured final solution.

    Reasoning:
    {state['reasoning_steps']}
    """
    state["final_output"] = gemini_generate(prompt)
    return state