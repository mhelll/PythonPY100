def pow_func(base, pow_=2):
    # base ** pow_ -> реализовать через цикл while
    res = 1
    while pow_ > 0:
        res = res * base
        pow_ -= 1

    return res


if __name__ == "__main__":
    a = 4
    n = 2
    print(pow_func(a, n))
