'''
[프로그래머스 입문코드 다루기]

프로그래머스 120816: 피자 나눠 먹기(3)
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120816
'''
def solution(slice, n):
    answer = 0
    
    if n % slice == 0:
        answer = n // slice
    else:
        answer = (n // slice) + 1
    return answer