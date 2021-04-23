# 자연수 n(1 이상 10**8 이하)이 매개변수로 입력됐을때, n을 3진법 상엥서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
# ex. n: 45 -> 7 
# ex. n: 125 -> 229

def solution(n):
    i=0
    while (n>3**(i+1)):
        i+=1
    print(i)
    res = []
    
    while i>=0:
        v = n//3**i
        res.append(v)
        n-=v*3**i
        i-=1
        print(n,v,i)
    answer = sum([3**i*v for i,v in enumerate(res)])
    
    return answer
  
  # 9/10 (한 케이스 통과하지 못함)
