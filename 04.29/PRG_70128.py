'''
[프로그래머스 Phase1 다루기]

프로그래머스 70128: 내적
URL : https://school.programmers.co.kr/learn/courses/30/lessons/70128
'''
def solution(a, b):
    answer = 0
    
    '''
    1. 일단 a, b 를 zip() 으로 묶은 다음에 for 문으로 변수 하나씩에 언패킹 해서 answer 에 저장
    2. 출력
    '''
    
    for a_num, b_num in zip(a, b):
        # += 식의 접근을 하게되면 매 루프마다 파이썬 인터프리터가 변수를 참조하고 값을 업데이트 하는 오버헤드가 발생함
        # 따라서 경량화로 다음과 같이 return 이 가능함
        answer += a_num * b_num
        
    return answer
    # 피드백 반영사항 : return sum(a_i * b_i for a_i, b_i in zip(a,b))

