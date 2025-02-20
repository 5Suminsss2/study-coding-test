# 소수 찾기 
# 내가 푼 답은 시간 초과 걸림 
def my_solution(n):
    answer = 0
    wow = 0
    for i in range(2,n+1):
        if (i==2):
            answer += 1
            continue
        for j in range(1,i+1):
            if (j != 1 and j != i):
                if (i%j ==0):
                    wow += 1
                    break
        if (wow==0):
            answer += 1
        else :
            wow = 0
        
    return answer



# 에라토스테네스의 체
def solution(n):
    if n < 2:
        return 0  # 2보다 작은 경우 소수 없음

    primes = [True] * (n + 1)  # 처음에는 모든 숫자를 소수(True)라고 가정
    primes[0] = primes[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):  # √n 이하의 숫자만 확인
        print(i, primes)
        if primes[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수를 전부 False로 만듦
                primes[j] = False

    return sum(primes)  # True로 남아 있는 개수(소수 개수) 반환