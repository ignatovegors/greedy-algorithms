from collections import Counter, namedtuple
import heapq


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.right.walk(code, acc + '0')
        self.left.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_coding(st):
    h = []
    for ch, freq in Counter(st).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def main():
    s = str(input())
    code = huffman_coding(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for key in sorted(code):
        print('{}: {}'.format(key, code[key]))
    print(encoded)


if __name__ == '__main__':
    main()
