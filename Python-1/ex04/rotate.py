import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def transpose(mat: list) -> list:
    """Returns the transposed matrix of a matrix"""
    try:
        tr = [[None] * len(mat) for x in range(len(mat[0]))]
        if (len(mat[0][0]) == 1):
            for i in range(len(tr)):
                for j in range(len(tr[0])):
                    tr[i][j] = mat[j][i][0]
        else:
            for i in range(len(tr)):
                for j in range(len(tr[0])):
                    tr[i][j] = mat[j][i]
        return (tr)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def main() -> int:
    """Cuts and flips animal.jpeg"""
    try:
        img = np.array(ft_load("animal.jpeg"))[100: 500, 400: 800, 0: 1]
        print("The shape of image is:", img.shape, "or", img.shape[0: 2])
        print(img)
        img = np.array(transpose(img))
        print("New shape after Transpose:", img.shape)
        print(img)
        plt.imshow(img, cmap="gray")
        plt.show()
        return (0)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (1)


if (__name__ == "__main__"):
    main()
