'''
“答案正确”是自动判题系统给出的最令人欢喜的回复。本题属于 PAT 的“答案正确”大派送 —— 只要读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”。
得到“答案正确”的条件是：
字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；
任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
现在就请你为 PAT 写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。

输入格式：
每个测试输入包含 1 个测试用例。第 1 行给出一个正整数 n (≤10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。
输出格式：
每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。
输入样例：
10
PAT
PAAT
AAPATAA
AAPAATAAAA
xPATx
PT
Whatever
APAAATAA
APT
APATTAA
输出样例：
YES
YES
YES
YES
NO
NO
NO
NO
NO
NO
'''
def rule(string):
    return rule1(string) and (rule2(string) or rule3(string))


def rule1(string):
    if string.count('P') != 1 or string.count('T') != 1:
        return False
    if string.index('P') > string.index('T'):
        return False
    for ch in string:
        if ch not in 'PAT':
            return False
    return True


def rule2(string):
    if 'PAT' == string:
        return True
    if string.count('PAT') != 1:
        return False

    index_PAT = string.index('PAT')
    x1 = string[:index_PAT]
    x2 = string[index_PAT + 3:]
    if x1 != x2:
        return False
    else:
        return True if x1.replace('A', '') == '' else False


def rule3(string):
    index_P = string.index('P')
    index_T = string.index('T')
    count_A = len(string[index_P + 1:index_T])
    if count_A == 0:
        return False
    while count_A > 1:
        index_T = string.index('T')
        if string[index_T - 1] != 'A':
            return False
        a = string[:index_P]
        c = string[index_T + 1:]
        if len(c) < len(a):
            return False
        string = string[:index_T - 1] + string[index_T:len(string) - len(a)]
        count_A -= 1
    return rule2(string)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        string = input()
        print('YES' if rule(string) else 'NO')
