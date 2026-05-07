'''
[프로그래머스 입문코드 다루기]

프로그래머스 120835: 진료순서 정하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120835
'''
def solution(emergency):
    # 1. 큰 순서대로 정렬된 기준 배열을 미리 하나 만든다.
    sorted_em = sorted(emergency, reverse=True)
    
    # 2. 원본 emergency를 순회(e)하면서, 정렬된 배열에서의 (위치 + 1)을 리스트에 담는다.
    return [sorted_em.index(e) + 1 for e in emergency]