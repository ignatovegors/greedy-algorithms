def valuable_backpack(backpack, capacity):
    tot_value = 0.0
    backpack.sort(reverse=True, key=custom_sort)

    for element in backpack:
        el_cost = element[0]
        el_volume = element[1]
        if capacity <= el_volume:
            tot_value += (float(capacity) / float(el_volume)) * el_cost
            break
        else:
            tot_value += el_cost
            capacity -= el_volume

    return tot_value


def custom_sort(a):
    return a[-1]


def main():
    backpack = []
    n, capacity = map(int, input().split())

    for i in range(n):
        cost, volume = map(int, input().split())
        backpack.append([cost, volume, float(cost) / float(volume)])

    print(valuable_backpack(backpack, capacity))


if __name__ == '__main__':
    main()
