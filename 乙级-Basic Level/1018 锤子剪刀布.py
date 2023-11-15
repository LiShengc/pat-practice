'''
现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。

输入格式：
输入第 1 行给出正整数 N（≤10^5），即双方交锋的次数。随后 N 行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。
C 代表“锤子”、J 代表“剪刀”、B 代表“布”，第 1 个字母代表甲方，第 2 个代表乙方，中间有 1 个空格。
输出格式：
输出第 1、2 行分别给出甲、乙的胜、平、负次数，数字间以 1 个空格分隔。
第 3 行给出两个字母，分别代表甲、乙获胜次数最多的手势，中间有 1 个空格。
如果解不唯一，则输出按字母序最小的解。
输入样例：
10
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J
输出样例：
5 3 2
2 3 5
B B
'''


class WinInfo:
    def __init__(self):
        self.counts = [0 for i in range(3)]

    def increase(self, gesture):
        self.counts[gestures.index(gesture)] += 1

    def most_index(self):
        max_count = max(self.counts)
        for i, count in enumerate(self.counts):
            if count == max_count:
                return i


if __name__ == '__main__':
    gestures = ['B', 'C', 'J']
    N = int(input())
    A_info = WinInfo()
    B_info = WinInfo()
    results = [0 for i in range(3)]
    for i in range(N):
        gesture_A, gesture_B = input().split()
        if gesture_A == gesture_B:
            # 平局
            results[1] += 1
            # results[1][1] += 1
        elif (gestures.index(gesture_A) + 1) % 3 == gestures.index(gesture_B):
            # A胜B负
            results[0] += 1
            A_info.increase(gesture_A)
        else:
            # A负B胜
            results[2] += 1
            B_info.increase(gesture_B)
    # 甲：胜平负
    print(' '.join(list(map(str, results))))
    # 乙：胜平负
    results.reverse()
    print(' '.join(list(map(str, results))))

    most_gesture = []
    print(gestures[A_info.most_index()] + ' ' + gestures[B_info.most_index()])
