def dif_terms(n):
    res = []
    i = 1
    while n - i >= i + 1:
        res.append(i)
        n -= i
        i += 1
    else:
        res.append(n)

    return res


def main():
    n = int(input())

    print(len(dif_terms(n)))
    print(*dif_terms(n))


if __name__ == '__main__':
    main()
