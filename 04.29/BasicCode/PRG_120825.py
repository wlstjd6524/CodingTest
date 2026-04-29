'''
[프로그래머스 입문코드 다루기]

프로그래머스 120825: 문자 반복 출력하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120825
'''
def solution(my_string, n):
    answer = ''
    
    for i in range(len(my_string)):
        answer += my_string[i] * n
        
    return answer