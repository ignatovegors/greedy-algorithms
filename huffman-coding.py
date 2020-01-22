def huffman_coding(st):
    freq_dic = dict()
    code_dic = dict()
    st_coded = ''

    for element in st:
        if element in freq_dic:
            freq_dic[element] += 1
        else:
            freq_dic[element] = 1
            code_dic[element] = ''

    if len(freq_dic) == 1:
        return [{st[0]: '0'}, '0' * len(st)]
    else:
        while len(freq_dic) >= 2:
            keys_list = sorted(list(freq_dic.keys()), key=lambda i: freq_dic[i])
            f0 = keys_list[0]
            f1 = keys_list[1]
            for element in f0:
                code_dic[element] += '0'
            for element in f1:
                code_dic[element] += '1'
            freq_dic[f0 + f1] = freq_dic[f0] + freq_dic[f1]
            freq_dic.pop(f0)
            freq_dic.pop(f1)

        for element in code_dic:
            code_dic[element] = code_dic[element][::-1]

        for element in st:
            st_coded += code_dic[element]

        return [code_dic, st_coded]


def main():
    st = str(input())

    res = huffman_coding(st)
    res_dic = res[0]
    res_st = res[1]

    print(len(res_dic), len(res_st))

    for element in res_dic:
        print(element, end=': ')
        print(res_dic[element])

    print(res_st)


if __name__ == '__main__':
    main()
