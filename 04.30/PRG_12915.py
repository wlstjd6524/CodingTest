'''
[프로그래머스 Phase1 다루기]

프로그래머스 12915: 문자열 내 마음대로 정렬하기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12915
'''
def solution(strings, n):
    '''
    1. 일단 strings 을 하나씩 뽑아서 그 문자에 [n] 번째 인덱스를 추출하고
    2. 그 추출한 인덱스를 저장하는 변수나 리스트를 만든 다음에 걔네를 오름차순으로 정렬
    3. 그다음에 그 단어들이 포함되어 있는 단어를 찾아보거나, 애초에 key 값으로 매핑할 수 있게 zip 으로 묶어야 되나?
    4. 그럼 짝꿍대로 그 단어를 순차적으로 append
    5. 출력
    '''
    
    '''
    피드백 1. 해당 로직대로 하면 만약 'cat' 이나 'car' 같이 두번 째 문장이 같은 경우에 에러로직을 처리하지 못하고
    컴퓨터가 방황할 수 있음
    피드백 2. 이름 없는 함수인 'lambda' 를 사용하여 이 문제를 해결 할 수 있음
    '''
    
    # 피드백 받은 상황으로 return 문을 꾸리면
    return sorted(strings, key=lambda x: (x[n], x))