# Programmers 위장 hash (level-2)

from itertools import combinations

def solution(clothes):
    type_cnt = {}
    for cloth in clothes:
        try:
            type_cnt[cloth[1]]+=1
        except KeyError:
            type_cnt[cloth[1]] = 1
    
    types = list(type_cnt.keys())
    answer = 0
    for i in range(1,len(types)+1):
        ans_add = 0
        for comb_tuple in combinations(types, i):
            ans_mul=1
            for j in range(i):
                ans_mul*=type_cnt.get(comb_tuple[j])
            ans_add+=ans_mul
        answer+=ans_add
    return answer
  
  
  # 1개가 time out됨... 최적화 필요!
