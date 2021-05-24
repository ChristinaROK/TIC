# Programmers 전화번호목록 level-2 hash

import copy
def solution(phone_book):
    answer = True
    while phone_book:
        first_num = phone_book.pop(0)
        first_set = {first_num}
        length = len(first_num)
        
        phone_book_cp = copy.deepcopy(phone_book)
        for num in phone_book_cp:
            if len(num)>length:
                break
            first_set.add(phone_book.pop(0))
        
        if first_set.intersection({num[:length] for num in phone_book}):
            answer = False
            break
            
    return answer
