# 1. python에서 dictionary 내부를 for문으로 돌 수 있다.
# 2. key와 vlaue 출력을 하기 위해서 이를 하기 위해서는 .items() 를 사용해야 한다.
# 3. replace 함수도 파이썬에 있지만 내가 간과한 것은 대체한 문자열을 다시 변수에 담아주지 않은 것, 꼭 담도록 하자


def solution(s):
    answer = 0
    numToChar={
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5", 
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }
    
    for key,value in numToChar.items():
        if key in s:
            s = s.replace(key,value)
            print("key, value", key, value)
            print("변경된 s",s)
        
    answer = int(s)
    
    return answer