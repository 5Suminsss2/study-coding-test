num = int(input())
i = 0
a = []

for i in range(num):
    age, name = input().split()
    a.append((int(age), name, i))
a.sort()
# print(a)
result = sorted(a, key=lambda x: (x[0], x[2]))

for i in range(num):
    print(result[i][0], result[i][1])
