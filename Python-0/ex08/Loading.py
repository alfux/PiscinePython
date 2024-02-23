def ft_tqdm(lst: range) -> None:
    """Copies the behavior of tqdm from tqdm module"""
    for i in lst:
        idx = lst.index(i)
        if idx < len(lst) - 1:
            percentage = int(100 * idx / len(lst))
        else:
            percentage = 100
        if percentage < 10:
            print("\r  " + str(percentage) + "%|[", end="")
        elif percentage < 100:
            print("\r " + str(percentage) + "%|[", end="")
        else:
            print("\r" + str(percentage) + "%|[", end="")
        bar = int(63 * percentage / 100)
        for j in range(bar):
            print("=", end="")
        print(">]", end="")
        for j in range(63 - bar):
            print(" ", end="")
        print("|", str(idx + 1) + "/" + str(len(lst)), end="")
        yield lst[idx]
