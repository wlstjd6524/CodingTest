'''
[프로그래머스 입문코드 다루기]

프로그래머스 120812: 최빈값 구하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120812
'''
def solution(array):
    # 파이썬에서 어떤 데이터의 빈도수(등장 횟수) 를 계산할 때는 가장 먼저 생각해야 할 요소는 '딕셔너리 사용'
    counts = {}
    
    for num in array:
        counts[num] = counts.get(num, 0) + 1
    
    # for 문을 통해 기록된 빈도수 중 가장 큰 값을 찾기
    max_count = max(counts.values())
    
    # 최댓값이랑 동일한 빈도수를 가진 '숫자(Key)' 들을 리스트로 추출 (리스트 컴프리헨션)
    modes = [key for key, value in counts.items() if value == max_count]
    
    # 최빈값이 2개 이상이면 -1, 아니면 최빈값 반환
    return -1 if len(modes) > 1 else modes[0]