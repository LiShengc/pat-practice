'''
令 P_i 表示第 i 个素数。现任给两个正整数 M ≤ N ≤ 10^4，请输出 P_M 到 P_N 的所有素数。

输入格式：
输入在一行中给出 M 和 N，其间以空格分隔。
输出格式：
输出从 P_M 到 P_N 的所有素数，每 10 个数字占 1 行，其间以空格分隔，但行末不得有多余空格。
输入样例：
5 27
输出样例：
11 13 17 19 23 29 31 37 41 43
47 53 59 61 67 71 73 79 83 89
97 101 103
'''

import math


def is_prime(num):
    if num <= 3:
        return num > 1
    if num % 6 not in [1, 5]:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    m, n = map(int, input().split(' '))
    primes = [2]
    num = 3
    while len(primes) <= n:
        if is_prime(num):
            primes.append(num)
        num += 1
    # print with format
    step = 10
    for i in range(m - 1, n, step):
        print(' '.join(map(str, primes[i:min(i + step, n)])))
