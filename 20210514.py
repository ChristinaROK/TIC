# Programmers 소수 만들기 (level-1)

from itertools import combinations

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

def solution(nums):
    return sum([prime(sum(cand)) for cand in combinations(nums, 3) if sum(cand)%2==1])
  
  
  # pass 
