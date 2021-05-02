# Programmers Greedy (level-2)

import string
def solution(name):
    upper = string.ascii_uppercase
    alpha_len = len(upper)
    cnt = {}
    
    for i, char in enumerate(upper):
        if alpha_len/2-i >0:
            cnt[char] = i
        else:
            cnt[char] = alpha_len-i
    
    answer = sum(cnt.get(char) for char in name)
    answer += min(len(name[0]+name[:0:-1].rstrip("A")),len(name.rstrip("A")))-1
            
    return answer

# 테스트 케이스 11번 통과 못함
# 나는 greedy와 관련 없이 풂

import string

def solution(name):
    upper = string.ascii_uppercase
    alpha_len = len(upper)
    cnt = {}
    
    # 1. up & down
    for i, char in enumerate(upper):
        if alpha_len/2-i >0:
            cnt[char] = i
        else:
            cnt[char] = alpha_len-i
    
    answer = sum(cnt.get(char) for char in name)
    
    # 2. left & right
    idx = 0
    half_len = len(name)//2
    move = 0
    togo = [i for i, x_ in enumerate(name) if x_ != "A" and i !=0]
    print(togo)
    while togo:
        if idx <= half_len: # right left 비교 필요
            r_m = togo[0] - idx
            l_m = len(name) - r_m
            if r_m < l_m: # go right
                move += r_m
                idx = togo[0]
                togo.pop(0)
                
            else: # go left
                move += len(name) - abs(togo[-1]-idx)
                idx = togo[-1]
                togo.pop()
            
        else:
            move += abs(togo[-1]-idx)
            idx = togo[-1]
            togo.pop()
               
    answer+=move
    return answer
# 테스트 케이스 4,5,7번 통과 못함
