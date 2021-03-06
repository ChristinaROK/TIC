# Programmers 전화번호목록 level-2 hash
# logic
# 1. 리스트를 길이 기준 오름차순 정렬 
# 2. 리스트를 순회 
# 2-1. end index를 +1 
# 2-2. 만약, 자신보다 길이가 긴 요소가 나오면, end index 기준으로 리스트의 앞, 뒤 요소의 교집합 찾기
# 2-3. 만약, 2-2에서 교집합이 존재한다면 answer=False 후 2를 종료
# 2-4. 만약, 2-2에서 교집합이 존재하지 않는다면 start index에 end index 값을 할당
# 2-4. end index가 리스트의 마지막 인덱스(len(list)-1)를 가리키면 2 순회 종료

def solution(phone_book):
    phone_book.sort(key=len)
    answer = True
    start = 0
    end = 0

    while end<len(phone_book)-1:
        l = len(phone_book[start])

        end+=1
        if len(phone_book[end])>l: # l보다 길이가 큰 요소 찾기
            if set(phone_book[start:end]).intersection([num[:l] for num in phone_book[end:]]): # l 길이 요소들이 l 길이보다 큰 요소들과 같은지 체크
                answer = False
                break
            else:
                start = end

    return answer

# pass 하지만 로직이 너무 어려움... 

# 남의 logic
# "접두사"가 되려면 요소(str)들의 첫 charcter끼리 무조건 같아야함
# 첫 character가 같으면, 두번째, 세번째, ... 작은 length의 character의 길이 만큼 character가 같아야함
# 결국 string의 list를 sorting하면 string의 character의 오름차순으로 정렬해줌. 
# 따라서 접두사가 같은 string끼리 모이게 됨

def solution(phone_book):
    phone_book.sort()
    answer = True
    
    for x, y in zip(phone_book, phone_book[1:]):
        if y.startswith(x):
            answer = False
            return answer
    return answer 
