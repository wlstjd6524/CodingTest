'''
[프로그래머스 입문코드 다루기]

프로그래머스 120829: 각도기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120829
'''
def solution(angle):
    if angle > 0 and angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle > 90 and angle < 180:
        return 3
    elif angle == 180:
        return 4