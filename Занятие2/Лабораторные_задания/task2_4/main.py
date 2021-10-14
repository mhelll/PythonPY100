if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    str_ = ["Hello,world"]
    for index, char in enumerate(str_, start=1):
        print(" "  * index + char)
