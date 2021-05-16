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

# Better => 모든 element를 list에 넣고 다시 pop할 필요가 없음. 
import math
def solution(progresses, speeds):
    Q = []
    for p,s in zip(progresses, speeds):
        d = math.ceil((100-p)//s)
        if (len(Q)==0) or (Q[-1][0]< d):
            Q.append([d, 1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
