'''
[프로그래머스 입문코드 다루기]

프로그래머스 120806: 두 수의 나눗셈
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120806
'''
def solution(num1, num2):
    # 문제 정의에 나눈 부분에 1000 을 곱한 다음에
    answer = (num1 / num2) * 1000
    
    # 곱한 부분의 정수 부분을 return 해야 하므로 answer 값의 int() 를 취하. 그러면 뒤에 float 형이 다 짤림
    answer = int(answer)
    return answer