'''
[프로그래머스 입문코드 다루기]

프로그래머스 120809: 배열 두 배 만들기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120809
'''
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[i] * 2)
    
    return answer