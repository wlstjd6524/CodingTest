'''
[프로그래머스 Phase1 다루기]

프로그래머스 12916: 문자열 내 p와 y의 개수
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12916
'''
def solution(s):
    s = s.upper()
    
    count_p = s.count('P')
    count_y = s.count('Y')
    
    if count_p == count_y:
        return True
    # 의문점1. 처음에 여기 조건문을 or 로 처리했는데 2개의 케이스가 탈락처리가 되서 문제 통과가 진행되지 않음.
    # 내가 or 을 준 이유는 어차피 p 또는 y 둘 중에 하나라도 문자열에 존재 하지 않으면 p 와 y 가 같은지 아닌지 비교가 안되기 때문에
    # 문제 조건에 따라 True 를 줘도 된다고 생각함. -> and 전환하고 모든 케이스가 통과해서 통과처리 됨.
    elif count_p == 0 and count_y == 0:
        return True
    else:
        return False
    
'''
    <-- 피드백 -->
    1. 해당 코드의 elif 문은 '데드코드' 임. 왜냐하면 애초에 조건문 자체가 if count_p == count_y 와 같은 말임 (문제 정의에 낚여서 의미 없는 코드 추가)
    따라서 해당 부분은 삭제해도 문제에 아무런 영향이 없음

    2. '데드코드' 에 대한 의문점을 해석하자면 or 을 줬을 때에는 이런 케이스가 발생 할 수 있음
        - 만약 단어에 'p' 가 존재하고 'y' 가 없다면 그것 또한 비교케이스임 그럼 p = 1 이고, y = 0 이기 때문에 두 개의 값이 다름 따라서
        - False 를 Return 해주는게 문제 정의상 맞는 이야기임

    3. 파이썬에서는 count_p == count_y 라는 수식자체가 Return 시 True False 를 뱉게 되어 있음.
    따라서 y 와 p 가 같은지만 비교하면 되는 쉬운 문제였으며, 이는 코드 2줄로 간단히 수정이 가능함


    <-- 피드백에 따른 수정 코드 -->
    s = s.upper()
    return s.count('P') == s.count('Y')
'''