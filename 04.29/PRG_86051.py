'''
[프로그래머스 Phase1 다루기]

프로그래머스 86051: 없는 숫자 더하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/86051
'''
def solution(numbers):
    '''
    1. 어차피 문제에 0 ~ 9 까지 숫자라고 제한했으니 일단 0 ~ 9 의 합인 45를 num 에 고정하고
    2. 없는 숫자의 합을 구하는 개념은 어차피 45 에서 있는 숫자의 합을 빼면 없는 숫자의 합이 되는거니까
    3. 고정한 num - numbers 의 합을 return 하면 정답발생.
    '''
    num = 45        
    number_sum = sum(numbers)
    
    answer = num - number_sum
    return answer

'''
피드백 1. 여러가지 변수를 만들어서 메모리를 차지할 필요가 없음. 따라서 이렇게 코드 경량화가 가능함
def solution(numbers):
    # 0~9 의 총합(45) 에서 현재 배열의 합을 뺀 결과를 즉시 반환
    return 45 - sum(numbers)
'''