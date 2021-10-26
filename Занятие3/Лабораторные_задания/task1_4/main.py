def task(epsilon=0.0001):
    sum_ = 0  # сумма бесконечного ряда
    n = 1
    item_n = 1 / 2 ** n # очередной элемент
    while item_n >= epsilon:
        sum_ += item_n
        n += 1
        item_n = 1 / 2 ** n

    while True:
        item_n = 1 / 2 ** n # очередной элемент
        if not (item_n >= epsilon):
            break

        sum_ += item_n
        n+1

    return sum_


if __name__ == "__main__":
    # Write your solution here
   print(task())
