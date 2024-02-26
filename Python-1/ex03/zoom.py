import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> int:
    """Displays "animal.jpeg" and prints some stats"""
    try:
        img = ft_load("animal.jpeg")
        print(img)
        img = img[100: 500, 450: 850, 0: 1]
        print("New shape after slicing:", img.shape, "or", img.shape[0: 2])
        print(img)
        plt.imshow(img, cmap="gray", vmin=0, vmax=255)
        plt.show()
        return (0)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)


if (__name__ == "__main__"):
    main()
