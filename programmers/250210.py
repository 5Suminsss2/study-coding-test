def solution(a, b, n):
    answer = 0

    while n >= a:  # 빈 병 개수가 a보다 작아질 때까지 반복
        new_cola = (n // a) * b  # 받을 수 있는 새로운 콜라 개수
        answer += new_cola  # 총 받은 콜라 개수 업데이트
        n = new_cola + (n % a)  # 마신 후 남은 빈 병 업데이트
    
    return answer