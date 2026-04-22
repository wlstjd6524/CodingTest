'''
[프로그래머스 입문코드 다루기]

프로그래머스 120811: 중앙값 구하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120811
'''
def solution(array):
    array.sort()
    
    return array[len(array)//2]