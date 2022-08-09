total, cutline = input().split()
a = list(map(int, input().split()))

a.sort(reverse=True)

print(a[int(cutline)-1])
