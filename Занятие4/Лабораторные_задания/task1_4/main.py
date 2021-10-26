def task(list_: list) -> list:
    mean = sum(list_) / len(list_)
    return [item for item in list_ if item > mean]
if __name__ == "__main__":
    print(task(list(range(10))))