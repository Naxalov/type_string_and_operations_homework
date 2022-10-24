def main(first,last):
    """
    Given two strings, first_name and last_name, return a single string in the format "last, first".
    Args:
        first: str
        last: str
    Returns:
        str: return answer.
    """
    full_name = last+', '+first
    return full_name


print(main('Zarif','Naxalov'))