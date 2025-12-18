def validate_user_input(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Please enter a valiad problem statement.")

    return text.strip()