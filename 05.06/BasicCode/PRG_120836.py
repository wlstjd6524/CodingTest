'''
[프로그래머스 입문코드 다루기]

프로그래머스 120836: 순서쌍의 개수
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120836
'''
def solution(n):
    count = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            
    return count