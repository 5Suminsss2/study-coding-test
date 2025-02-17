# 가장 가까운 같은 글자

def solution(s):
    answer = []
    num = 0

    for i in range(len(s)):
        # 하나씩 돌아가면서 위치 찾기
        current = i
        
        if (current != 0):
            for j in reversed(range(current)):
                if (s[j] == s[i]):
                    num = i - j
                    if (num < 0):
                        num = -num
                    answer.append(num)
                    break
                if (j == 0 and s[j] != s[i]):
                    answer.append(-1)
            # if (num == 0): # 이렇게 하면 위의 코드에서 -1 추가 되고 또 -1이 추가됨
            #     answer.append(-1)
                    
        else:    
            # 첫번재 요소이면 무조건 -1 추가
            answer.append(-1)
        print("==answer",answer)
    
    return answer