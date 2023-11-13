import time

n = int(input())
names = []
nos = []
scores = []
infos = []
t1 = time.time()
for i in range(n):
    info, score = input().rsplit(maxsplit=1)
    # name, no, score = input().split()
    # names.append(name)
    # nos.append(no)
    infos.append(info)
    scores.append(score)

best = max(scores)
worst = min(scores)
best_index = scores.index(best)
# print(names[best_index], ' ', nos[best_index])
# print(names[best_index] + ' ' + nos[best_index])
print(infos[best_index])

worst_index = scores.index(worst)
# print(names[worst_index] + ' ' + nos[worst_index])
print(infos[worst_index])

t2 = time.time()
print('消耗时间' + str(t2 - t1))

t1 = time.time()
best_score = 0
worst_score = 100
for i in range(n):
    if int(score) > best_score:
        best_score = int(score)
        best_info = info
    if int(score) < worst_score:
        worst_score = int(score)
        worst_info = info
print(best_info)
print(worst_info)
t2 = time.time()
print('消耗时间' + str(t2 - t1))
