# **참고**

num = int(input())
a = list(map(int, input().split()))

i = 0
result = set(a)
final = list(result)
final.sort()

numdict = {}
for i in range(len(final)):
    numdict[final[i]] = i
    #print(i, numdict)

for i in a:  # 새로 알게 된 부분
    print(numdict[i], end=' ')

# print(final)
# print(numdict)
