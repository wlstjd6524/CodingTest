'''
[프로그래머스 입문코드 다루기]

프로그래머스 120818: 옷가게 할인 받기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120818
'''
def solution(price):
    answer = 0
    
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000 and price < 500000:
        answer = price * 0.9
    elif price >= 100000 and price < 300000:
        answer = price * 0.95
    else:
        answer = price
    
    return int(answer)