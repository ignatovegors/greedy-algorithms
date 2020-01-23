def insert(lst, number):
    lst.append(number)
    k = len(lst)
    while k != 1 and lst[k // 2 - 1] < number:
        temp = lst[k // 2 - 1]
        lst[k // 2 - 1] = number
        lst[k - 1] = temp
        k = k // 2

    return lst


def extract(lst):
    print(lst[0])
    lst[0] = -1
    k = len(lst)
    i = 1
    while 2 * i <= k:
        if 2 * i == k:
            temp = lst[i - 1]
            lst[i - 1] = lst[2 * i - 1]
            lst[2 * i - 1] = temp
            i *= 2
        else:
            if lst[2 * i - 1] > lst[2 * i]:
                temp = lst[i - 1]
                lst[i - 1] = lst[2 * i - 1]
                lst[2 * i - 1] = temp
                i *= 2
            else:
                temp = lst[i - 1]
                lst[i - 1] = lst[2 * i]
                lst[2 * i] = temp
                i = 2 * i + 1


def main():
    lst = []
    n = int(input())

    for i in range(n):
        command = str(input())
        if command.startswith('Insert'):
            number = int(command.split()[1])
            lst = insert(lst, number)
        elif command == 'ExtractMax':
            extract(lst)


if __name__ == '__main__':
    main()
