import numpy as np
import matplotlib.image as img


def ft_load(path: str) -> np.array:
    """Opens an image file into a ndarray and prints it shape before return"""
    try:
        pic = img.imread(path)
        print("The shape of image is:", pic.shape)
        return (pic)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)
