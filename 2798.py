# **참고**

n, m = map(int, input().split())
a = list(map(int, input().split()))

total = 0
result = []

for i in range(n-2):
    for j in range(n-2):
        for k in range(n-2):
            #print(i, j+1, k+2)
            #print("합 : ", a[i], a[j+1], a[k+2])
            total = a[i] + a[j+1] + a[k+2]
            if(total <= m and i != j+1 and i != k+2 and j+1 != k+2):
                result.append(total)

result.sort()
# print(result)
print(result[len(result)-1])
