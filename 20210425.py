# Programmers Hash (level-1)
# participant (list) 중 통과하지 못한 1명의 사람 이름을 반환하시오. 단, 통과한 사람의 개수는 len(participant)-1로 completion(list)이다.

from collections import Counter
def solution(participant, completion):
    for i in Counter(participant) - Counter(completion):
        return i
# 통과!
