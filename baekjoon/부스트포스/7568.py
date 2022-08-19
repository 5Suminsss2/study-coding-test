n = int(input())

weight = []
height = []
result = []
for i in range(n):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

for i in range(n):
    result.append(1)

#print(weight, height)
for i in range(n):
    for j in range(n):
        # print(i,weight[i],j,weight[j],i,height[i],j,height[j])
        if(weight[i] < weight[j] and height[i] < height[j]):
            # print(i,j)
            result[i] = result[i] + 1

# print(result)

for i in result:
    print(i, end=" ")
