'''
[프로그래머스 입문코드 다루기]

프로그래머스 120819: 아이스 아메리카노
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120819
'''
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer