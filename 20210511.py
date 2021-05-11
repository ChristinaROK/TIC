# Programmers 비밀 지도 (level-1)

# def binary(x,n,res):
#     i=n
#     while 2**i>x:
#         i-=1

#     res.append(i)

#     if x-(2**i)==0:
#         return res
#     return binary(x-(2**i), n, res)
def binary(x):
    return [i for i, s_ in enumerate(bin(x).replace('0b','')[::-1]) if s_ =="1"]

def solution(n, arr1, arr2):
    answer = []
    for x1, x2 in zip(arr1, arr2):
        res = set.union(set(binary(x1)), binary(x2))

        answer_ = [" "]*n
        for i in res:
            answer_[i] = "#"
        answer.append("".join(reversed(answer_)))

    return answer
  
  
  # pass
  # binary 직접 구현하다가 run-time error나서 bin 내장 함수 씀 ㅠㅠ 
  # 쉬운 문제를 너무 어렵게 생각했음...

# better code!
def binary(x):
    return bin(x)[2:]
    
def solution(n, arr1, arr2):
    answer = []
    for x1, x2 in zip(arr1, arr2):
        a = str(int(binary(x1)) + int(binary(x2))).zfill(0)
        answer_ = ""
        for a_ in a:
            if a_ == "0":
                answer_+=" "
            else:
                answer_+="#"
        answer.append(answer_)
        
        
    return answer
