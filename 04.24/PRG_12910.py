'''
[프로그래머스 Phase1 다루기]

프로그래머스 12910: 나누어 떨어지는 숫자 배열
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12910
'''
def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    
    if len(answer) == 0:
        return [-1]
    
    answer.sort()
    
    # 리스트 컴프리 헨션을 사용하여 푼다면 이런 방식으로 풀 수가 있음. (앞으로는 이런 방식을 쓰도록 유도해야함)
    '''
        # arr 에서 요소(x) 를 하나씩 꺼내가지고 divisor 로 나누어 떨어지는 것만 리스트로 만들고
        answer = [x for x in arr if x % divisor == 0]
        
        # answer 가 비어있지 않으면 정렬해서 반환하면 되고, 비어있으면 [-1] 을 반환
        return sorted(answer) if len(answer) != 0 else [-1]
    '''
    return answer