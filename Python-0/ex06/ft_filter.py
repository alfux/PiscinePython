def ft_filter(function, iterable) -> list:
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if (function is None):
        return ([elem for elem in iterable if elem])
    return ([elem for elem in iterable if function(elem)])
