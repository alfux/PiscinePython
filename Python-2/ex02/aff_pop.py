import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from load_csv import load


def to_number(x: str) -> float:
    """Converts a srting with M or K units into a float."""
    try:
        x.strip()
        if ('B' in x):
            return (float(x.strip('B')) * 1000000000)
        if ('M' in x):
            return (float(x.strip('M')) * 1000000)
        if ('k' in x):
            return (float(x.strip('k')) * 1000)
        return (float(x))
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def millions(x, pos) -> str:
    """Returns a million unit formatter for the plot's y axis."""
    return (f"{x * 1e-6:1.0f}M")


def main() -> int:
    """Displays and compares populations."""
    try:
        data = load("population_total.csv").set_index("country")
        data = data.map(to_number)
        xaxis = data.columns.astype(int)[0: 251]
        ax = plt.subplot()
        ax.yaxis.set_major_formatter(millions)
        ax.yaxis.set_major_locator(tck.MultipleLocator(20e6))
        ax.xaxis.set_major_locator(tck.MultipleLocator(40))
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plots = plt.plot(xaxis, data.loc["Madagascar"][0: 251], "#0088AA",
                         xaxis, data.loc["France"][0: 251], "g")
        plt.legend(plots, ["Madagascar", "France"], loc="lower right")
        plt.show()
        return (0)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (1)


if (__name__ == "__main__"):
    main()
