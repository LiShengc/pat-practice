'''
某城镇进行人口普查，得到了全体居民的生日。现请你写个程序，找出镇上最年长和最年轻的人。
这里确保每个输入的日期都是合法的，但不一定是合理的——假设已知镇上没有超过 200 岁的老人，
而今天是 2014 年 9 月 6 日，所以超过 200 岁的生日和未出生的生日都是不合理的，应该被过滤掉。

输入格式：
输入在第一行给出正整数 N，取值在(0,10^5]；
随后 N 行，每行给出 1 个人的姓名（由不超过 5 个英文字母组成的字符串）、以及按 yyyy/mm/dd（即年/月/日）格式给出的生日。
题目保证最年长和最年轻的人没有并列。
输出格式：
在一行中顺序输出有效生日的个数、最年长人和最年轻人的姓名，其间以空格分隔。
输入样例：
5
John 2001/05/12
Tom 1814/09/06
Ann 2121/01/30
James 1814/09/05
Steve 1967/11/20
输出样例：
3 Tom John
'''
from datetime import datetime

if __name__ == '__main__':
    n = int(input())
    oldest = datetime(2014, 9, 7)
    youngest = datetime(1814, 9, 6)
    datetimes = [youngest, oldest]
    valid_count = 0
    year_now, month_now, day_now = list(map(int, '2014/9/6'.split('/')))
    for i in range(n):
        name, birthday = input().split()
        birthday = datetime(*list(map(int, birthday.split('/'))))
        # 过滤晚于 2014/9/6 和 超过200岁（即早于 1814/9/6）
        if birthday < datetimes[0] or birthday > datetimes[1]:
            continue
        valid_count += 1
        if birthday < oldest:
            oldest = birthday
            oldest_name = name
        if birthday > youngest:
            youngest = birthday
            youngest_name = name
    print(' '.join(list(map(str, [valid_count, oldest_name, youngest_name]))))
