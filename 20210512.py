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
# string을 구별하는 기준을 변하지 않는 유일한 조건인 (S,D,T)로 설정함

import operator
pow_dic = {"S":1, "D":2, "T":3}


def solution(dartResult):
    i=0
    s = dartResult
    res = []
    while len(s)>0:

        if len(s)==1: # s only contains *,#
            if s[0] == "*":
                res[-2:] = [n*2 for n in res[-2:]]
            elif s[0] == "#":
                res[-1]*=-1
            return sum(res)

        if s[i] in pow_dic.keys():
            if s[0] in ["*","#"]:
                if s[0] == "*":
                    res[-2:] = [n*2 for n in res[-2:]]
                elif s[0] == "#":
                    res[-1]*=-1
                s=s[1:]
                i-=1
            res.append(operator.pow(int(s[:i]), int(pow_dic[s[i]])))
            s = s[i+1:]
            i=0

        else:
            i+=1
    return sum(res)
# 통과!!
