#Programmers hash 위장 (level-2) re!!!
# 경우의 수를 물어봤기 때문에 combination 사용할 필요가 없었음...
from itertools import combinations

def solution(clothes):
    type2cloth = {} 
    for cloth in clothes:
        try:
            type2cloth[cloth[1]]+=1
        except KeyError:
            type2cloth[cloth[1]] = 1

    answer = 1
    for num in type2cloth.values():
        answer*=(num+1)

    return answer-1
