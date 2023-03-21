n, m = map(int, input().split())
li = list(map(int, input().split()))

li2 = []

for i in range(len(li)):
  for j in range(i+1, len(li)):
    for k in range(j+1, len(li)):
      total = 0
      total = li[i] + li[j] + li[k]
      li2.append(total)

      if(total > m):
        li2.pop()
        break

li2.sort()
print(li2[-1])


