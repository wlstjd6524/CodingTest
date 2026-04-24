'''
[프로그래머스 입문코드 다루기]

프로그래머스 120817: 배열의 평균값
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120817
'''
def solution(numbers):
    len_num = len(numbers)
    
    sum = 0
    for i in range(len_num):
        sum += numbers[i]
    
    return sum / len_num