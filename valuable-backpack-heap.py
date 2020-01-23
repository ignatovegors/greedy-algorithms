import sys
import heapq


def valuable_backpack(goods, capacity):
    order = [(-value / weight, weight) for value, weight in goods]
    heapq.heapify(order)

    tot_value = 0.0
    while order and capacity:
        vpw, weight = heapq.heappop(order)
        can_take = min(weight, capacity)
        capacity -= can_take
        tot_value -= vpw * can_take

    return tot_value


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    goods = list(reader)
    print('huy')

    print(valuable_backpack(goods, capacity))


if __name__ == '__main__':
    main()
