'''
本题要求计算 A/B，其中 A 是不超过 1000 位的正整数，B 是 1 位正整数。你需要输出商数 Q 和余数 R，使得 A=B×Q+R 成立。

输入格式：
输入在一行中依次给出 A 和 B，中间以 1 空格分隔。
输出格式：
在一行中依次输出 Q 和 R，中间以 1 空格分隔。
输入样例：
123456789050987654321 7
输出样例：
17636684150141093474 3
'''


def div(a, b):
    for i, digit in enumerate(a):
        if digit != '0':
            break
    a, b = a[i:], int(b)
    if b == 1:
        return a, str(b)
    Q, r = '', ''
    for i, digit in enumerate(a):
        num = int(r + digit)
        q, r = list(map(str, [num // b, num % b]))
        Q += q
    for i, digit in enumerate(Q):
        if digit != '0':
            break
    return Q[i:], r


if __name__ == '__main__':
    A, B = input().split()
    print(' '.join(div(A, B)))

    # print(' '.join(list(map(lambda op: str(eval(A + op + B)), ['//', '%']))))
