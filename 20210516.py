# Programmers (level-2) stack&queue 기능개발

import math
def solution(progresses, speeds):
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    answer = []
    while len(days)>0:
        s = days.pop(0)
        i=1
        while len(days)>0:
            if days[0]<=s:
                days.pop(0)
                i+=1
            else:
                break
        answer.append(i)

    return answer
  
  # pass! 
