# Programmers (level-2) 더맵게 Heap (Priority Queue)

import heapq

def solution(scoville, K):
    
#     if sum(scoville)**(len(scoville)-1) < K:
#         return -1 
    
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
  
# pass
# line7 => 1억개의 int를 sum하는 cost가 상당해서 효율성에서 pass하지 못했음 
# scoville 요소 개수만큼 (max 1억) push & pop하는 것이 효율성면에서 좋음 
