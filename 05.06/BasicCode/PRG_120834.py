'''
[프로그래머스 입문코드 다루기]

프로그래머스 120834: 외계행성의 나이
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120833
'''
def solution(age):
    # 피드백 1. age 를 str 로 만들어서 순회하고
    # 피드백 2. 각 문자 i 를 다시 정수 int 로 바꿔서 97(ord('a')) 를 더한 뒤 chr() 로 문자로 변환
    # 피드백 3. 그 조각들을 "".join() 으로 압축
    return "".join(chr(ord('a') + int(i)) for i in str(age))