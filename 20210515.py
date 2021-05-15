# Programmers (level-2) 더맵게 Heap (Priority Queue)

import heapq

def solution(scoville, K):
    
    if sum(scoville)**(len(scoville)-1) < K:
        return -1 
    
    heapq.heapify(scoville)
    answer = 0    
    min1 = heapq.heappop(scoville)
    
    while min1<K:
        try:
            min2=heapq.heappop(scoville)
        except IndexError:
            return -1
        min1 = heapq.heappushpop(scoville, min2*2+min1)
        answer+=1
    
    return answer
  
  # 효율성에서 -4 
