'''
本题要求编写程序，计算 2 个有理数的和、差、积、商。

输入格式：
输入在一行中按照 `a1/b1 a2/b2` 的格式给出两个分数形式的有理数，其中分子和分母全是整型范围内的整数，负号只可能出现在分子前，分母不为 0。
输出格式：
分别在 4 行中按照 `有理数1 运算符 有理数2 = 结果` 的格式顺序输出 2 个有理数的和、差、积、商。
注意输出的每个有理数必须是该有理数的最简形式 `k a/b`，
    其中 k 是整数部分，`a/b` 是最简分数部分；若为负数，则须加括号；若除法分母为 0，则输出 `Inf`。
题目保证正确的输出中没有超过整型范围的整数。
输入样例 1：
2/3 -4/2
输出样例 1：
2/3 + (-2) = (-1 1/3)
2/3 - (-2) = 2 2/3
2/3 * (-2) = (-1 1/3)
2/3 / (-2) = (-1/3)
输入样例 2：
5/3 0/6
输出样例 2：
1 2/3 + 0 = 1 2/3
1 2/3 - 0 = 1 2/3
1 2/3 * 0 = 0
1 2/3 / 0 = Inf
'''


class RationalNumber:
    def __init__(self, a, b):
        self.a, self.b = int(a), int(b)
        self.sign = -1 if self.a < 0 else 1
        self.a = abs(self.a)
        self.k = 0

    def simplify(self):
        k = self.a // self.b
        a = self.a % self.b
        c = gcd(self.a, self.b)
        a, b = list(map(lambda x: int(x / c), [a, self.b]))
        return self.sign, k, a, b

    def tongfen(self, other):
        b = self.b * other.b
        a1 = self.a * other.b + self.k * b
        a2 = other.a * self.b + other.k * b
        return a1, a2, b

    def add(self, other):
        a1, a2, b = self.tongfen(other)
        a = self.sign * a1 + other.sign * a2
        return str(RationalNumber(a, b))

    def sub(self, other):
        return self.add(RationalNumber(-1 * other.sign * other.a, other.b))

    def mul(self, other):
        a = (self.a + self.k * self.b) * (other.a + other.k * other.b)
        b = self.b * other.b
        sign = self.sign * other.sign
        return str(RationalNumber(sign * a, b))

    def div(self, other):
        if other.iszero():
            return 'Inf'
        return self.mul(RationalNumber(other.sign * other.b, other.a))

    def iszero(self):
        return True if self.a == 0 and self.k == 0 else False

    def __str__(self):
        if self.iszero():
            return '0'
        sign, k, a, b = self.simplify()
        res = []
        if k != 0:
            res.append(f'{k}')
        if a != 0:
            res.append(f'{abs(a)}/{b}')
        res = ' '.join(res)
        if sign == -1:
            res = '(-' + res + ')'
        return res


# 求两数的最大公约数：辗转相除法
def gcd(a, b):
    a = a % b
    return b if a == 0 else gcd(b, a)


if __name__ == '__main__':
    r1, r2 = input().split()
    r1 = RationalNumber(*r1.split('/'))
    r2 = RationalNumber(*r2.split('/'))
    print(f'{r1} + {r2} = {r1.add(r2)}')
    print(f'{r1} - {r2} = {r1.sub(r2)}')
    print(f'{r1} * {r2} = {r1.mul(r2)}')
    print(f'{r1} / {r2} = {r1.div(r2)}')
