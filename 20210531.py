#Programmers 소수 찾기 (level-2)

from itertools import permutations
from math import sqrt,ceil

def prime(number):
    
    if number ==1:
        return 0
    
    if number in [3,5,7]:
        return 1
    
    for i in range(3, ceil(sqrt(number)), 2):
        if number%i == 0:
            return 0
    return 1

            
def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        for number_string in permutations(numbers, r=i):
            number_int = int("".join(number_string))
            if number_int%2!=0:
                if number_int not in answer:
                    answer.append(number_int)
    print([prime(number) for number in answer])               
    return sum([prime(number) for number in answer])
 
# 정확도 50 ㅠ
