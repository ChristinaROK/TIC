# Programmers 문자열 압축 (level-2)

def solution(s):
    ori=s
    max_len = len(ori)//2
    answer = 0

    while max_len > 0: # max greedy
        left_str_len = 0
        
        while len(s) >0: # find v(equal cnt) for each pattern substrings
            pattern = s[:max_len]
            
            idx = max_len
            v = 0
            while True:
                if pattern == s[idx:2*idx]:
                    v+=1
                    idx+= max_len
                else:
                    break      
            
            if v > 0:
                answer+=len(str(v))+max_len
            else:
                left_str_len += len(pattern)
            s = s[idx:]
            
        if answer>0:
            return answer+left_str_len
        else:
            s = ori
            max_len-=1
    return len(ori)
