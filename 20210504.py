# Programmers 로또 최고 순위와 최저 순위 (level-1) 

def solution(lottos, win_nums):
    res = 0

    for n in win_nums:
        if n in lottos:
            res+=1
    max = 7-res if res>1 else 6

    res+=lottos.count(0)
    min = 7-res if res>1 else 6

    answer = [min,max]
    return answer
