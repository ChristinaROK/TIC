# Programmers 모의고사 완전탐색 (level-1)

def solution(answers):
    length = len(answers)
    a = [i for i in range(1,6)]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    list_func = lambda x : x*(length//len(x)) + x[:length%len(x)]

    res = [0,0,0]
    for ans, a, b, c in zip(answers, list_func(a), list_func(b), list_func(c)):
        abc = [a,b,c]
        for i in range(3):
            res[i] += int(ans == abc[i])

    answer = []
    v = 0
    for i, x in enumerate(res):
        if v < x:
            v = x
            answer = [i+1]
        elif v == x:
            answer.append(i+1)

    return answer
  
  # 성공!
