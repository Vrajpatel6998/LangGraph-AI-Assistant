import streamlit as st
from graph.graph_builder import build_graph
from utils.validators import validate_user_input

st.set_page_config(page_title="LangGraph AI Assistant")

st.title("🤖 LangGraph AI Assistant")

problem = st.text_area("Enter your problem statement")

if st.button("Generate Solution"):
    try:
        # Validate user input
        cleaned_input = validate_user_input(problem)

        # Build and invoke the graph
        graph = build_graph()
        result = graph.invoke({"user_input": cleaned_input})

        # Display results
        st.subheader("🧠 Reasoning Steps")
        st.write(result["reasoning_steps"])

        st.subheader("✅ Final Answer")
        st.success(result["final_output"])

    except ValueError as ve:
        # Input validation errors
        st.error(str(ve))

    except Exception as e:
        # Other runtime errors
        st.error(f"Unexpected error: {str(e)}")
