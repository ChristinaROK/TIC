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
