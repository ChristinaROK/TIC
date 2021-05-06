# Programmers 오픈채팅방 level-2

def solution(record):
    id2name = {}
    res = []

    for history in record:
        h_list = history.split()

        if h_list[0] in ["Enter","Change"]:
            id2name[h_list[1]]=h_list[-1]

        if h_list[0] == "Enter":
            res.append(f"{h_list[1]},님이 들어왔습니다.")
        elif h_list[0] == "Leave":
            res.append(f"{h_list[1]},님이 나갔습니다.")

    answer = [id2name[txt.split(",")[0]]+txt.split(",")[1] for txt in res ]


    return answer
  
  # 통과!
