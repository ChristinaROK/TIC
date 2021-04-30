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
# Pass

# Programmers 실패율, (level-1)

from collections import Counter

def solution(N, stages):
    staying_users = Counter(stages)
    staying_users = dict(sorted(staying_users.items(), key=lambda item: item[0]))
    tot = len(stages)
    res = {}
    for stage, n in staying_users.items():
        res[stage] = (n / tot)
        tot-=n
    return sorted([i for i in range(1,N+1)], key = lambda x : res.get(x, 0), reverse=True)

# Pass
