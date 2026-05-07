'''
[프로그래머스 Phase1 다루기]

프로그래머스 17681: [1차] 비밀지도 - 카카오 기출문제
URL : https://school.programmers.co.kr/learn/courses/30/lessons/17681
'''
def solution(n, arr1, arr2):
    return [bin(a | b)[2:].zfill(n).replace('1', '#').replace('0', ' ') for a, b in zip(arr1, arr2)]