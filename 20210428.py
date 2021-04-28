# Programmers 모의고사 완전탐색 (level-1)

def solution(answers):
    length = len(answers)
    a = [i for i in range(1,6)]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    list_func = lambda x : x*(length//len(x)) + x[:length%len(x)]

    res = [0,0,0]
    for ans, a, b, c in zip(answers, list_func(a), list_func(b), list_func(c)):
        abc = [a,b,c]
        for i in range(3):
            res[i] += int(ans == abc[i])

    answer = []
    v = 0
    for i, x in enumerate(res):
        if v < x:
            v = x
            answer = [i+1]
        elif v == x:
            answer.append(i+1)

    return answer
  
# 성공!
# list max value idx return 코드 개선
# answers의 길이만큼 후보 리스트 3개를 늘릴 필요가 없음. 따라서 answers의 length를 미리 알 필요 없이 idx를 length까지 +1하며 늘려나감

def solution(answers):
    candidates = [[i for i in range(1,6)],
                  [2,1,2,3,2,4,2,5],
                  [3,3,1,1,2,2,4,4,5,5]]
    res = [0] * len(candidates)
    
    ### answers 인덱스를 +1 하며 candidate 점수를 채워가기
    for idx, ans in enumerate(answers):
        for iidx, candidate in enumerate(candidates):
            res[iidx] += int(ans == candidate[idx%len(candidate)])

    ### initial 값을 max로 설정 ###
    max_value = max(res)
    answer = sorted([i+1 for i, v in enumerate(res) if max_value == v])

    return answer
