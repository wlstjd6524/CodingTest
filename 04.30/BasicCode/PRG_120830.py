'''
[프로그래머스 입문코드 다루기]

프로그래머스 120830: 양꼬치
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120830
'''
def solution(n, k):
    answer = (n * 12000) + (abs(n // 10 - k) * 2000)
    return answer