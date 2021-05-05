# Programmers 문자열 압축 (level-2)

def solution(s):
    
    answer = len(s)
    
    for patternLen in range(1,len(s)//2+1):
        ss = s # ss is changing
        pattern = ss[:patternLen]
        answer_ = 0
        
        while len(ss)>0:
            
            prefix = 0
            while True: # pattern matching
                
                if pattern == ss[:patternLen]: # 일치 pattern count
                    prefix+=1
                    ss = ss[patternLen:]
                else:
                    break
                   
            # 정산
            if prefix>1:
                answer_+=len(str(prefix))+len(pattern)
            else:
                answer_+=len(pattern)
                    
            # pattern 넘겨주기 
            pattern = ss[:patternLen]
                
        answer = min(answer, answer_)
        
    return answer

 # Pass
    
# Better Solution! 
# step size만큼 list index를 이동하는 방법을 step size만큼 잘라놔 list에 넣고 list index +1을 보는 방법으로 구현한 것이 신박함! 

def compress(s, patternLen):
    words = [s[i:i+patternLen] for i in range(0,len(s),patternLen)]
    cur_word = words[0]
    cur_cnt = 1
    res = []
    
    for a, b in zip(words, words[1:]+[""]):
        if a==b:
            cur_cnt+=1
        else:
            res.append([cur_word, cur_cnt])
            cur_word=b
            cur_cnt=1

    return sum(len(word)+(len(str(cnt)) if cnt>1 else 0) for word, cnt in res)

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        answer = min(answer, compress(s, i))
        
    return answer
