'''
[프로그래머스 입문코드 다루기]

프로그래머스 120808: 분수의 덧셈
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120808
'''
import math

def solution(numer1, denom1, numer2, denom2):
    # 1. 분모를 서로 곱하여 통분하고 분자를 더함
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    
    # 2. 분자와 분모의 최대공약수를 구함
    # 이 때 사용하는 함수 math.gcd() -> 유클리드 호제법을 내부적으로 사용하여 O(log(n)) 의 빠른 시간을 가짐
    gcd_value = math.gcd(numer, denom)
    
    # 최대공약수로 나눠서 기약분수로 만든 후 리스트로 반환
    return [numer // gcd_value, denom // gcd_value]