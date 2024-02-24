import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices from start to everything before end"""
    try:
        arr = np.array(family)
        print("My shape is :", arr.shape)
        arr = arr[start: end]
        print("My new shape is :", arr.shape)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
    return (arr.tolist())
