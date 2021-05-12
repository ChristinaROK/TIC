# Programmers [1차 다트게임] (level-1)

import operator
pow_dic = {"S":1, "D":2, "T":3}

def solution(dartResult):
    
    alph_idx = [i for i, s in enumerate(dartResult) if s in pow_dic.keys()]
    
    start_idx = [0]
    for i in range(1, len(alph_idx)):
        offset = alph_idx[i]-alph_idx[i-1]
        if offset in [2,3]:
            start_idx.append(alph_idx[i]-1)
        elif offset == 4:
            start_idx.append(alph_idx[i]-2)
    
    res = []
    for s,e in zip(start_idx, start_idx[1:]+[len(dartResult)]):
        s = dartResult[s:e]
        if s[-1] in pow_dic.keys():
            n = operator.pow(int(s[:-1]), pow_dic[s[-1]])
        else:
            n = operator.pow(int(s[:-2]), pow_dic[s[-2]])
            if s[-1] == "*":
                if len(res)>0:
                    res[-1] = res[-1]*2
                n*=2
            elif s[2] == "#":
                n*=-1
        res.append(n)

    return sum(res)
  
# 통과 못함 ....why???
