'''
读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

输入格式：
每个测试输入包含 1 个测试用例，即给出自然数 n 的值。这里保证 n 小于 10^100。
输出格式：
在一行内输出 n 的各位数字之和的每一位，拼音数字间有 1 空格，但一行中最后一个拼音数字后没有空格。
输入样例：
1234567890987654321123456789
输出样例：
yi san wu
'''

if __name__ == '__main__':
    num_pinyin = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
    print(' '.join([num_pinyin[int(i)] for i in str(sum([int(num) for num in input()]))]))
    # for i, num in enumerate(str(count)):
    #     if i == len(str(count)) - 1:
    #         end = '\n'
    #     else:
    #         end = ' '
    #     print(num_pinyin[int(num)], end=end)
