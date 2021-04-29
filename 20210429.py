# Programmers 신규 아이디 추천 String Operation (Level-1)

import re
def solution(new_id):
    pattern = r'[^0-9a-z._\-]'
    answer = re.sub(pattern, '', new_id.lower())
    answer = re.sub(r'\.+', '.', answer)
    answer = re.sub(r'^\.|\.$', '', answer)
    if len(answer) ==0:
        answer = "a"
    elif len(answer)>=16:
        answer = answer[:15]
        answer = re.sub(r'\.$', '', answer)
    if len(answer) <= 2:
        answer += answer[-1] * (3-len(answer))

    return answer
