# Programmers 예산, (level-1)

def solution(d, b):
    d.sort()
    answer = 0
    for i in d:
        b -=i
        if(b<0):
            break
        answer +=1
    return answer
