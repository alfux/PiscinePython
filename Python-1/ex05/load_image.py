import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.array:
    """Opens an image file into a ndarray and prints its shape before return"""
    try:
        pic = img.imread(path)
        print("The shape of image is:", pic.shape)
        print(pic)
        plt.imshow(pic)
        plt.show()
        return (pic)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)
