# **참고**

n = int(input())
total = 0
for i in range(1, n+1):
    nums = list(map(int, str(i)))
    result = i + sum(nums)
    if(result == n):
        total = i
        break

print(total)
