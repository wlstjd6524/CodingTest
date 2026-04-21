'''
[프로그래머스 Phase1 다루기]

프로그래머스 42748: K번째수
URL : https://school.programmers.co.kr/learn/courses/30/lessons/42748
'''
def solution(array, commands):
    '''
    # 개념이 2차원 배열에 들어가 있는 3개의 원소가 i,j,k 를 가져가니까
    # 2차원 배열에 진입해서 2차원 배열의 첫 번째 리스트에 들어가면 거기서 0번째 인덱스가 i, 그다음 인덱스가 j
    # 마지막 인덱스가 k 인 방식으로 진행
    for g in commands:
        for h in commands:
            # 이렇게 범위를 하드코딩 해도 된다고 생각 한 이유는 문제에 'commands' 의 각 원소는 길이가 3이라고 정의함.
            i = commands[g][h]
            j = commands[g][h+1]
            k = commands[g][h+2]
            
            # i,j,k 가 정해진 상태에서 array 처리 로직 시작.
            array = array[i:j]
            array.sort()
            return array[k]
    '''
    # 피드백 받은 상황대로 코드 정리
    answer = []

    # commadns 안의 [i, j, k] 리스트를 바로 i, j, k 변수로 분해해서 가져오기
    for i, j, k in commands:
        # 1. i-1 부터 j 까지 자르고 정렬
        sliced_arr = sorted(array[i-1:j])
        # 2. k-1 번째 요소를 정답 배열에 추가
        answer.append(sliced_arr[k-1])

    return answer