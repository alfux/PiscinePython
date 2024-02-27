import numpy as np
import matplotlib.pyplot as plt


def ft_invert(ar: np.array) -> np.array:
    """Inverts the color of the image received."""
    try:
        arr = 255 - np.array(ar)
        print("The shape of image is:", arr.shape)
        print(arr)
        plt.imshow(arr)
        plt.show()
        return (arr)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def ft_red(ar: np.array) -> np.array:
    """Keeps only red in the image received."""
    try:
        arr = [1, 0, 0] * np.array(ar)
        print("The shape of image is:", arr.shape)
        print(arr)
        plt.imshow(arr)
        plt.show()
        return (arr)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def ft_green(ar: np.array) -> np.array:
    """Keeps only green in the image received."""
    try:
        arr = np.array(ar)
        for i in arr:
            for j in i:
                j.itemset(0, 0)
                j.itemset(2, 0)
        print("The shape of image is:", arr.shape)
        print(arr)
        plt.imshow(arr)
        plt.show()
        return (arr)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def ft_blue(ar: np.array) -> np.array:
    """Keeps only blue in the image received."""
    try:
        arr = np.array(ar)
        for i in arr:
            for j in i:
                j.itemset(0, 0)
                j.itemset(1, 0)
        print("The shape of image is:", arr.shape)
        print(arr)
        plt.imshow(arr)
        plt.show()
        return (arr)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def ft_grey(ar: np.array) -> np.array:
    """Puts the image received in shades of grey"""
    try:
        arr = np.array(ar)
        for i in arr:
            for j in i:
                shade = j.sum() / 3
                j.fill(shade)
        print("The shape of image is:", arr.shape)
        print(arr)
        plt.imshow(arr)
        plt.show()
        return (arr)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)
