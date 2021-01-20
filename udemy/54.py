def example_func(params1, params2):
    """Example function with types documented in the docstring.
    Args:
        params1 (int): The first parameter.
        params2 (str): The second parameter.

    Returns:
        boot: The return value. True for success, False otherwise.
    """
    print(params1)
    print(params2)
    return True

print(example_func.__doc__)

