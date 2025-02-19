# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    sum = 0
    for i in range(len(numbers)):
        print(i)
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if (sum in answer) :
                continue
            else:
                answer.append(sum)
                
    answer.sort()
    return answer


# 리스트에 해당 값이 있나요 ? : value in [리스트]
    # js에 익숙해져서 includes를 사용하게 된다.
    # 하지만 python에서는 in 이라는 간단한 요소를 사용하면 된다!! 기억하자!!

# 오름차순 정렬 방법 : [리스트].sort()
    # 내림차순은 [리스트].sort(reverse=True) 