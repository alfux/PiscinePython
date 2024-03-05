class statistics:
    """Computes and stores a float iterable's statistics."""
    def __init__(self, *args, **kwargs):
        """Stores data for computations."""
        self._data = sorted(args)
        self._len = len(args)

    @property
    def mean(self) -> float:
        """Computes mean of self._data."""
        mean = 0
        for x in self._data:
            mean += x
        return (float(mean / len(self._data)))

    @property
    def median(self) -> float | int:
        """Finds median value in self._data."""
        if (self._len % 2):
            return (self._data[self._len // 2])
        else:
            return (float(self._data[(self._len // 2) - 1] +
                          self._data[self._len // 2]) / 2)

    @property
    def quartile(self) -> list[float]:
        """Finds 1st and 3rd quartiles in self._data."""
        if (self._len % 4):
            return ([float(self._data[self._len // 4]),
                     float(self._data[3 * self._len // 4])])
        else:
            return ([float(self._data[self._len // 4 - 1]),
                     float(self._data[3 * self._len // 4 - 1])])

    @property
    def var(self) -> float:
        """Computes variance of self._data."""
        mean = self.mean
        var = 0
        for x in self._data:
            var += (x - mean) ** 2
        return (float(var / self._len))

    @property
    def std(self) -> float:
        """Computes standard deviation of self._data."""
        return (float(self.var ** 0.5))


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Prints statistics on args according to kwargs.

    The function uses <args> to compute estimators.
    Any key can be used in <kwargs>, only the values are read.
    Accepted values are:
        'mean' 'median' 'quartile' 'std' 'var'
    """
    try:
        stat = statistics(*args, **kwargs)
        for kw in kwargs.values():
            try:
                match kw:
                    case "mean":
                        print(f"mean : {stat.mean}")
                    case "median":
                        print(f"median : {stat.median}")
                    case "quartile":
                        print(f"quartile : {stat.quartile}")
                    case "std":
                        print(f"std : {stat.std}")
                    case "var":
                        print(f"var : {stat.var}")
            except BaseException:
                print("ERROR")
    except BaseException as err:
        print(f"{err.__class__.__name__}: {err}")
