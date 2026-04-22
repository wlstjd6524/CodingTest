'''
[프로그래머스 입문코드 다루기]

프로그래머스 120813: 짝수는 싫어요
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120813
'''

def solution(n):
    answer = []
    
    for i in range(n+1):
        if i % 2 != 0:
            answer.append(i)
        
    return answer