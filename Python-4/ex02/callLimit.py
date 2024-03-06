def callLimit(limit: int):
    """Returns a decorator depending on <limit>."""
    count = 0

    def callLimiter(function):
        """Wraps <function> to add a call limit."""
        def limit_function(*args: any, **kwds: any):
            """Limited <function>."""
            nonlocal count
            nonlocal limit
            if (count < limit):
                count += 1
                function(*args, **kwds)
            else:
                print(f"Error: <function {function.__name__}", end=' ')
                print(f"at 0x{id(function):x}> call too many times")
        return (limit_function)
    return (callLimiter)
