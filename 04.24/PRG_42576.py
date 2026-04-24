'''
[프로그래머스 Phase1 다루기]

프로그래머스 42576: 완주하지 못한 선수
URL : https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''
def solution(participant, completion):
    # 딕셔너리의 key:value 형식으로 비교하면 좋을 것 같은데
    # 문제는 어떤식으로 매핑하냐의 고민이 생김. 
    
    # 참가자 : 통과자 식으로 해야할까? 아니면 참가자 딕셔너리 따로, 통과자 딕셔너리를 따로한 다음에
    # 그 두개의 딕셔너러리를 비교하는 형식으로 해야할까?
    hash_dict = {}
    
    # 1. 참가자 기록 (동명이인 이면 숫자가 2, 3 으로 올라감)
    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1
        
    # 2. 완주자는 빼버림
    for c in completion:
        hash_dict[c] -= 1
    
    # 3. 값이 0이 아닌 사람 (완주하지 못한 사람을 의미) 찾기
    for key, value in hash_dict.items():
        if value > 0:
            return key