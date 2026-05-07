'''
[프로그래머스 Phase1 다루기]

프로그래머스 42840: 모의고사
URL : https://school.programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    # 1. 톱니바퀴 패턴 정의
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 2. 채점: enumerate로 인덱스(i)와 정답(a)을 뽑고, 각 패턴의 순환 인덱스와 비교하여 sum
    scores = [
        sum(1 for i, a in enumerate(answers) if a == p1[i % len(p1)]),
        sum(1 for i, a in enumerate(answers) if a == p2[i % len(p2)]),
        sum(1 for i, a in enumerate(answers) if a == p3[i % len(p3)])
    ]
    
    # 3. 1등 가려내기: 최고 점수(max)와 같은 점수를 받은 사람의 번호(인덱스+1)만 추출
    return [i + 1 for i, score in enumerate(scores) if score == max(scores)]