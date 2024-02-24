import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int, float]) -> list[int | float]:
    """Computes a list of Body Mass Index values"""
    try:
        bmi = np.array([height, weight])
        return ((bmi[1] / (bmi[0] ** 2)).tolist())
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Compares bmi values against limit"""
    try:
        bmi = np.array(bmi)
        return ((bmi > limit).tolist())
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)
