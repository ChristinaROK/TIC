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

# pass

# better version
# 1. deque (double ended queue)는 맨 앞, 맨 뒤 삽입 삭제의 시작 복잡도가 O(1)이다. 
# 2. location index의 출력 순서가 answer이기 때문에 res를 만들 필요 없이 rotation하지 않으면 answer에 +1하고 cur index와 location이 일치하면 반환 
from collections import deque
def solution(priorities, location):
    queue = deque([(i,v) for i,v in enumerate(priorities)])
    answer=0
    while True:
        cur = queue.popleft()
        if any(cur[1]<q[1] for q in queue):
            queue.append(cur)
        else:
            answer+=1
            if location==cur[0]:
                return answer
