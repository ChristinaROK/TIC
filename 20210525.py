# Programmers 문자열 내 p와 y의 개수 (level-1) 

import re
def solution(s):
    return len(re.findall(r'[Pp]',s)) == len(re.findall(r'[Yy]',s))

# pass
# s.lower()후 s.count("p") 할 수도 있음
