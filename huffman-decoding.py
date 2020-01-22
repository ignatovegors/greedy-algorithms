def huffman_decoding(dic, st):
    decoded_st = ''

    while len(st):
        for i in range(1, len(st) + 1):
            if st[:i:] in dic:
                decoded_st += dic[st[:i:]]
                st = st[i::]
                break

    return decoded_st


def main():
    dic = {}

    n, k = map(int, input().split())

    for i in range(n):
        letter, code = map(str, input().split(': '))
        dic[code] = letter

    st = str(input())

    print(huffman_decoding(dic, st))


if __name__ == '__main__':
    main()
