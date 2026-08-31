def attempts_to_score(attempts: int) -> int:
    """
    This function get attempts and return a score with a some way.
    """
    score = 350
    score = score - (attempts * 50)

    return score