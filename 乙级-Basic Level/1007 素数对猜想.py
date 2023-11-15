'''
让我们定义 d_n 为：`d_n = p_n+1 − p_n`，其中 p_i 是第 i 个素数。显然有 d_1 = 1，且对于 n > 1 有 d_n 是偶数。
“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。
现给定任意正整数N(<10^5 )，请计算不超过N的满足猜想的素数对的个数。

输入格式:
输入在一行给出正整数N。
输出格式:
在一行中输出不超过N的满足猜想的素数对的个数。
输入样例:
20
输出样例:
4
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
    n = int(input())
    last_prime = 2
    count_prime_pair = 0

    for num in range(3, n + 1):
        if is_prime(num):
            if num - last_prime == 2:
                count_prime_pair += 1
            last_prime = num
    print(count_prime_pair)
