# Programmers 괄호 회전하기 (level2)
# 파라미터 s를 x번 (1<=x<=len(s)) 왼쪽으로 회전할 때 s가 옮은 문자열이 된 횟수를 출력하시오.
# 옮은 문자열이란 "()", "{}", "[]"이며, 옮은 문자열이 A일 때, "(A)", "{A}", "[A]"도 옮은 문자열이며 A,B가 옳은 문자열일 때, AB 역시 옳은 문자열이다.

import collections
partner = {"(" : ")", "[" : "]", "{" : "}", ")" : "(", "]" : "[", "}" : "{"}
partner_sort = {"(" : ")", "[" : "]", "{" : "}"}

def solution(s):
    # 1. Is partner counted the same? 
    s_dict = collections.Counter(s)
    for key, value in s_dict.items():
        if value != s_dict.get(partner.get(key)):
            return 0
    # 2. Is partner arrangement correct? (ex. "(" precedes ")")
    answer = 0
    for i in range(len(s)):
        fail = False
        
        if i>0:
            s = s[1:] + s[0]
        
        for start, end in partner_sort.items():
            start_idx = s.find(start)
            
            if start_idx<0:
                break
                
            end_idx = s.find(end)
            if (start_idx > end_idx):
                fail = True
                break
                
        if not fail:
            answer+=1
            
    return answer

# time complexity 통과 못함
