# Programmers Greedy (level-2)

import string
def solution(name):
    strings = string.ascii_uppercase
    s_len = len(strings)
    cnt = {}
    
    for i, char in enumerate(strings):
      if (s_len/2) - i > 0:
        cnt[char]=i
      else:
        cnt[char]=s_len-i
    
    # ing ...
    return answer

  # ing
