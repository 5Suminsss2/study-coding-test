a = int(input())
i = 0
word = []

for i in range(a):
    b = input()
    word.append(b)

result = list(set(word))
result.sort()
result.sort(key=len)

total_num = len(result)
for i in range(total_num):
    print(result[i])
