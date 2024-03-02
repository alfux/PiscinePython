import matplotlib.pyplot as plt
from load_csv import load


def to_number(x: str) -> float:
    """Converts numbers with KMB into real floats"""
    try:
        if (x.__class__ != str):
            return (x)
        if ('K' in x or 'k' in x):
            return (float(x.strip('Kk')) * 1e3)
        if ('M' in x or 'm' in x):
            return (float(x.strip('Mm')) * 1e6)
        if ('B' in x or 'b' in x):
            return (float(x.strip('Bb')) * 1e9)
        return (float(x))
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def thousands(x: float, pos: float) -> str:
    """Formatter to have thousands as k numbers"""
    try:
        return (f"{x * 1e-3:1.0f}k")
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (None)


def main() -> int:
    """Plots life expectancy against gross domestic product"""
    try:
        x = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        x = x.set_index("country").map(to_number)
        y = load("life_expectancy_years.csv")
        y = y.set_index("country").map(to_number)
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross domestic product")
        plt.title("1900")
        plt.xscale("log")
        plt.subplot().xaxis.set_major_formatter(thousands)
        plt.scatter(x["1900"].astype(int), y["1900"], marker=".", s=150)
        plt.legend(["Country"], loc="lower right")
        plt.show()
        return (0)
    except BaseException as err:
        print(err.__class__.__name__ + ":", err)
        return (1)


if (__name__ == "__main__"):
    main()
