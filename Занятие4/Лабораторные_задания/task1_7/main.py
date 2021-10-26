def task(list_: list) -> list:
    mean = sum(list_) / len(list_)
    return [item for item in list_ if item - mean]
if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(task(list_))



