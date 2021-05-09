# Programmers 메뉴 리뉴얼 (level-2)

from itertools import combinations

def solution(orders, course):
    # 1. 후보군 메뉴 (최소 2 팀이 식사를 한 메뉴) 추리기
    menu_cands = set([frozenset(set(orders[i])&set(orders[j])) for i in range(len(orders)) for j in range(i+1,len(orders))])

    answer = []
    for num in course:
        # 2. course(메뉴수)별로 menu_cands에서 조합을 통해 uniq 메뉴를 선정
        num_menu = []
        for menu in menu_cands:
            num_menu.extend(list(combinations(menu, num)))
        num_menu = list(set(num_menu))

        # 3. num_menu (메뉴수의 uniq 메뉴)별 max 주문 횟수의 메뉴 정하기
        max_cnt = 0
        res = []
        for menu in num_menu:
            cnt = sum([set(menu).issubset(set(order)) for order in orders])
            if cnt>max_cnt:
                res=["".join(sorted(menu))]
                max_cnt=cnt
            elif cnt==max_cnt:
                res.append("".join(sorted(menu)))

        # 4. 메뉴 담기 
        answer.extend(res)
    return sorted(answer)

# test case는 통과인데 나머지는 35/100점...
# 꼭 다시 풀 것
[참고](https://gee05053.tistory.com/18)
