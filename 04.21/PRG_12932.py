'''
[프로그래머스 Phase1 다루기]

프로그래머스 12932: 자연수 뒤집어 배열로 만들기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12932
'''
def solution(n):
    answer = []
    str_n = str(n)
    
    for char in str_n:
        answer.append(int(char))
    
    return answer[::-1]

'''
    <-- 피드백 -->
    1. 해당 문제는 '리스트 컴프리헨션' 을 통해 코드 경량화가 가능함

    <-- 피드백에 따른 수정 코드 -->
    # 해석 : n을 문자열로 바꾸고 뒤집은 다음에 [::-1], 그 다음 요소 하나하나를 int 로 변환해서 List 로 묶기.
    return [int(char) for char in str(str(n))[[::-1]]]
'''