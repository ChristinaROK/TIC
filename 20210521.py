# Programmers 다리를 지나는 트럭 stack&queue (level-2) 

def solution(bridge_length, weight, truck_weights):
    truck_cnt = [[weight, 0] for weight in truck_weights]
    answer = 0
    on_load = []

    while (answer == 0) or (len(on_load)>0):
        answer+=1

        if answer==1:
            on_load.append(truck_cnt.pop(0))

        # remove finished truch
        if on_load[0][1]>=bridge_length:
            on_load.pop(0)

        # append new truck?
        if len(truck_cnt)>0 and sum([truck[0] for truck in on_load])+truck_cnt[0][0] <= weight:
            on_load.append(truck_cnt.pop(0))

        # add cnt to on_load trucks
        for truck in on_load:
            truck[1]+=1
    return answer
  
  # pass
