# Programmers 2016년 윤년 (level-1)

def solution(a, b):
    days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    weekday = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}

    return weekday[(sum([days[month] for month in range(1, a)]) + b - 1) % 7]
    return answer

  # 통과
