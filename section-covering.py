def section_covering(a):
    a.sort(key=sort_custom)
    res = []

    right_side = a[0][1]
    res.append(right_side)

    for element in a:
        left_side_temp = element[0]
        right_side_temp = element[1]
        if not (left_side_temp <= right_side <= right_side_temp):
            right_side = element[1]
            res.append(right_side)

    return res


def sort_custom(a):
    return a[-1]


def main():
    a = []
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())
        a.append([x, y])

    print(len(section_covering(a)))
    print(*section_covering(a))


if __name__ == '__main__':
    main()
