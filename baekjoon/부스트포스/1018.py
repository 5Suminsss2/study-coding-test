# **참고**

n, m = map(int, input().split())
init = []
result = []
# 초기 체스판
for i in range(n):
    init.append(input())

# 체스판 구성
for i in range(n-7):
    for j in range(m-7):
        first_w = 0
        first_b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if((k+l) % 2 == 0):
                    if(init[k][l] != 'W'):
                        first_w += 1  # w로 시작하는데 짝수는 시작하는 곳의 색깔과 똑같아야 함
                    if(init[k][l] != 'B'):
                        first_b += 1
                else:
                    if(init[k][l] != 'W'):
                        first_b += 1  # w로 시작하는데 홀수는 시작하는 곳의 색깔과 겹쳐서는 안됨
                    if(init[k][l] != 'B'):
                        first_w += 1
        result.append(first_w)
        result.append(first_b)

print(min(result))
