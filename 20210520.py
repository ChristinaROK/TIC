# Programmers 프린터 stack/queue (level-2)

def solution(priorities, location):
    tup = [(v,i) for i,v in enumerate(priorities)]
    res = []
    while len(tup)>0:
        max_v = max(tup)[0]
        v, i = tup.pop(0)
        if v!=max_v:
            tup.append((v,i))
        else:
            res.append(i)
    answer = res.index(location)+1
    return answer
