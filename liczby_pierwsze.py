def znajdz_pierwsze_n_liczb_pierwszych(n: int):
    liczby_pierwsze = []
    num = 2
    while len(liczby_pierwsze) < n:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                liczby_pierwsze.append(num)
        num += 1
    return liczby_pierwsze


if __name__ == '__main__':
    N = 20
    print(znajdz_pierwsze_n_liczb_pierwszych(5))