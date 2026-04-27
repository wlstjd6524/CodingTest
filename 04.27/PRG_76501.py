'''
[프로그래머스 Phase1 다루기]

프로그래머스 76501: 음양 더하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/76501
'''
def solution(absolutes, signs):
    '''
    answer = 0
    
    # 일단 두개의 리스트를 zip () 으로 묶어
    zip_list = zip(absolutes, signs)
    
    # 묶은 다음에 매핑된 부분에서 signs 리스트에서 true 로 매핑된건 그냥 그대로 나오고
    # false 로 매핑된 부분은 음수로 치환해서 나와야 함.
    
    # 근데 묶은 파일을 어떻게 접근해야 하는지 감이 안잡힘..
    '''
    
    # 피드백 1. zip 으로 묶어서 num 과 sing 이라는 변수로 언패킹 하면서 순회
    # 피드백 2. sign 이 True 면 num, False 면 -num 으로 변환해서 리스트(제너레이터) 생성
    # 피드백 3. sum() 으로 모든 요소의 합을 계산
    return sum(num if sign else -num for num, sign in zip(absolutes, signs))