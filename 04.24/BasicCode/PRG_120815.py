'''
[프로그래머스 입문코드 다루기]

프로그래머스 120815: 피자 나눠 먹기(2)
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120815
'''
def solution(n):
    i = 1
    
    while (6 * i) % n != 0:
        i += 1
    
    return i