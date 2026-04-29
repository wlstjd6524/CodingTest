'''
[프로그래머스 Phase1 다루기]

프로그래머스 68644: 두 개 뽑아서 더하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/68644
'''
def solution(numbers):
    answer = []
    
    '''
    1. 일단 이중 for 문으로 numbers 에 있는 모든 인덱스를 다 더한걸 answer 에 넣고
    2. answer 에 중복값이 생길거임 그럼 그거를 set() 으로 중복제거하고, sort() 로 오름차순 정렬하고
    3. 출력하면 됨.
    '''
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
            
    # 피드백 받은 부분, 원래는 sort() 를 먼저 한 다음에 set 을 list 로 덮었는데 그렇게 진행하면 기껏 정렬했는데 set() 으로 다시 혼동을 주는거라
    # 몇 개의 케이스는 통과하겠지만 몇 개의 케이스는 통과하지 못하는 예외가 발생 할 수 있음
    # 따라서 set() 으로 먼저 흔들어놓고, sort() 로 정렬하는게 바람직함.        
    answer = list(set(answer))
    answer.sort()
    
    return answer

'''
피드백을 받고 수정한 사항
1. 파이썬에는 itertools.combinations 라는 라이브러리가 존재함 이 부분으로 코드 경량화가 가능함

from itertools import combinations

def solution(numbers):
    # 1. numbers 에서 2개를 뽑는 모든 조합 comb 를 생성하고
    # 2. 각 조합의 합 (sum(comb)) 를 구하고
    # 3. set 으로 중복 제거하고, sorted 로 정렬해서 반환
    return sorted(set(sum(comb) for comb in combinations(numbers, 2)))
'''