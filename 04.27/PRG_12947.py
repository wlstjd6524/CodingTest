'''
[프로그래머스 Phase1 다루기]

프로그래머스 12947: 하샤드 수
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12947
'''
def solution(x):
    '''
    # 먼저 Split 할 수 있게 받은 정수형 x 를 문자형으로 바꿔주고
    str_x = str(x)
    
    # 그다음에 for char in x: 형태로 각 Split 한 문자를 받아 줄 리스트선언
    split_list = []
    
    # Split 문자 받고
    for char in x:
        # 근데 여기서 코드를 더 줄일 수 있을 것 같은데 내가 for char in x: 로직이 한 번에 "1", "8" 이 뽑히는지
        # 아니면 순차적으로 뽑히는지 몰라서 일단 구현을 목표로 리스트에 안전하게 넣고 그걸 정수화 시켜서 각 자리 수
        # 더한 다음에 더해서 나온 값이 x 랑 나눠떨어지는지 알아보려고 함
        split_list.append(x)
    
    # 그다음 split_list 를 정수화 시키고
    split_list = list(map(int, split_list))
    
    # 쟤 합계를 변수에 넣고
    answer = sum(split_list)
    
    # 이 변수를 이제 x 랑 나눠서 나눠 떨어지면 true, 안나눠 떨어지면 false
    if x % answer == 0:
        return True
    else:
        return False
    '''
    
    # 피드백 1. 위 문제에서 for char in x: 에서 str_x 라는 문자열 변수를 잘 만들어 놓고도 다시 정수형 x로 뽑아서 타입 에러를 발생시킴
    # 피드백 2. 따라서 split_list.append(x) 에서도 str_x 를 넣어야 하는데 또 정수형 x 를 넣고 있음
    # 피드백 3. 무엇보다 '리스트 컴프리헨션' 을 사용하면서 파이썬 근육을 키워야 하는데 아직도 C/JAVA 식 코딩에 머물러 있음
    
    # 1. str(x) 를 순회하면서 문자(char) 를 하나씩 꺼내서,
    # 2. 곧바로 int(char) 로 전환해서 리스트 만들고, sum() 으로 합 구하기
    digit_sum = sum([int(char) for char in str(x)])
    
    # 3. 나누어 떨어지는지 여부를 곧바로 반환
    return x % digit_sum == 0