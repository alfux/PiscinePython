import matplotlib.pyplot as plt
from load_csv import load


def main() -> int:
    """Displays a graph France's data from the .csv file."""
    try:
        data = load("life_expectancy_years.csv")
        data.set_index("country", inplace=True)
        plt.ylabel("Life expectancy")
        plt.xlabel("Year")
        plt.title("France Life expectancy Projections")
        plt.plot(data.columns.astype(int, copy=False), data.loc["France"])
        plt.show()
        return (0)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (1)


if (__name__ == "__main__"):
    main()
