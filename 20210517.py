# Programmers 주식 가격 (level2) stack queue

def solution(prices):
    answer = []
    n_stocks = len(prices)
    
    while n_stocks>0:
        p = prices.pop(0)
        n_stocks-=1
        i=0
        sec=0
        while i<n_stocks:
            sec+=1
            if prices[i]<p:
                break
            i+=1
        answer.append(sec)
        
    return answer
  
  # 효율성 테스트 통과 못함
