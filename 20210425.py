# Programmers Hash (level-1)
# participant (list) 중 통과하지 못한 1명의 사람 이름을 반환하시오. 단, 통과한 사람의 개수는 len(participant)-1로 completion(list)이다.

from collections import Counter
def solution(participant, completion):
    for i in Counter(participant) - Counter(completion):
        return i

# hash를 사용한 코드 (남의 코드)
def solution(participant, completion):
    tot = 0
    dic = {}
    for name in participant:
        tot+=hash(name)
        dic[hash(name)]=name
    for name in completion:
        tot-=hash(name)
    return dic[tot]

# 통과!
