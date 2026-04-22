'''
[프로그래머스 Phase1 다루기]

프로그래머스 12935: 제일 작은 수 제거하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12935
'''

'''
    <-- 맨 처음 생각해보고 풀어본 로직 -->
    def solution(arr):
    # 빈 배열이면 계산할 필요가 없으니 일단 arr 길이가 1인지 부터 확인하고 빈배열이면 -1 Return
    if len(arr) == 1:
        return -1
    
    # 빈 배열이 아니면 일단 정렬하고
    arr.sort()
    answer = []
    
    # 첫 번째 인덱스만 제거, remove() 를 써보려고 했는데 얘는 리스트 요소를 전체 다 지우는 것 같아서
    # for 문으로 arr 길이만큼 돌리는데 1번째 인덱스부터 받기
    i = 1
    for i in range(len(arr) + 1):
        answer.append(i)
    
    # 다시 거꾸로 출력
    return answer[::-1]

    <-- 피드백 -->
    1. sort() 를 할 경우 Return 해야 하는 변수가 오름차순으로 정렬되서 출력형식에 맞지 않아 아예 망가져버림
    2. for 문 자체에 에러가 발생함. 선언 케이스대로 하면 for 문 안에 있는 부분은 우리가 선언한 리스트를 아예 쳐다보지 않아 모든 값을 넣어버리는
    케이스가 발생함
'''

# 따라서 파이썬에서 존재하는 remove() 와 min() 으로 코드 경량화가 가능함
def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    # 리스트에서 최소값을 찾아서 제거하기 min() 함수
    arr.remove(min(arr))
    
    return arr