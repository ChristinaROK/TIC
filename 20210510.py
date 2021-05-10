# Programmers 키패드 누르기 (level-1)

def distance(x,y):
    dis=0
    for i,j in zip(x,y):
        dis+=abs(i-j)
    return dis

def solution(numbers, hand):
    idx_dict = {}
    idx_dict[0] = (3,1)
    for i in range(3):
        for j in range(3):
            idx_dict[3*i+(j+1)] = (i,j)

    left = (3,0)
    right = (3,2)
    answer = ''
    for n in numbers:
        if idx_dict[n][1] == 0:
            answer+="L"
            left = idx_dict[n]
        elif idx_dict[n][1] == 2:
            answer+="R"
            right = idx_dict[n]
        else:
            left_dis = distance(left, idx_dict[n])
            right_dis = distance(right, idx_dict[n])
            if left_dis>right_dis:
                answer+="R"
                right = idx_dict[n]
            elif left_dis<right_dis:
                answer+="L"
                left = idx_dict[n]
            elif left_dis==right_dis:
                answer+= hand[0].upper()
                if hand[0].upper() == "R":
                    right = idx_dict[n]
                else:
                    left = idx_dict[n]
    return answer
  
# pass!
