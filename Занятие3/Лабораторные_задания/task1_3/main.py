def func_(a: int) -> list:
    list_sipmle_number = []
    for current_number in range(a + 1):
        m = 0
        for n in range(1, current_number + 1):
            if current_number % n == 0:
                m = m + 1
            if m == 2:
                list_sipmle_number.append(current_number)

            return list_sipmle_number

def func_1(number, list_prime_number):
    prime_factors = []
    while number != 1:
        for prime_number in list_prime_number:
            while number % prime_number == 0:
                prime_factors.append(prime_number)
                number = number // prime_number

    return prime_factors


if __name__ == "__main__":
    s = 63
    list_ = func_(s)
    print(list_)
    list_1 = func_1(s, list_)
    print(list_1)