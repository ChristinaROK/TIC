# Programmers Stack 크레인 인형뽑기 (level-1)


def solution(board, moves):
    board.reverse()

    col = {}
    for i, x in enumerate(zip(*[row for row in board])):
        col[i+1] = [x_ for x_ in x if x_>0]

    answer = 0
    res = []
    for m in moves:
        if col[m]: 
            v = col[m].pop()
            if len(res)>0 and res[-1] == v:
                res.pop()
                answer+=2
            else:
                res.append(v)
        else:
            continue

    return answer
  
  # Pass
