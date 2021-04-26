# Programmers 정렬 가장 큰 수 (level-2)
# numbers 수가 입력됐을 때 가장 큰 수로 정렬해 string으로 반환하라

def solution(numbers):
    str_num = [str(n) for n in numbers]
    # max_len = max([len(n) for n in str_num])
    max_len = 4
    offset = lambda x : x + x*(max_len-len(x)) if max_len>2*len(x) else x + x[:max_len-len(x)] 
    return str(int("".join(sorted(str_num, key=offset, reverse=True))))

