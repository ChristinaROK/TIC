# Programmers 문자열 압축 (level-2)

def solution(s):
    ori=s
    max_len = len(ori)//2
    answer = len(ori)

    while max_len > 0: 
        sub_answer = 0
        left_str_len = 0

        while len(s) >0: # find v(equal cnt) for each pattern substrings
            pattern = s[:max_len]

            idx = max_len
            v = 1
            while True:
                if pattern == s[idx:idx+max_len]:
                    v+=1
                    idx+= max_len
                else:
                    break      

            if v > 1:
                sub_answer+=len(str(v))+max_len
            else:
                left_str_len += len(pattern)
            s = s[idx:]

        if sub_answer>0:
            answer = min(answer, sub_answer + left_str_len)
        s = ori
        max_len-=1
    return answer


 # Pass
