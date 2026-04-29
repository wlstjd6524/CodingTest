'''
[프로그래머스 입문코드 다루기]

프로그래머스 120824: 짝수 홀수 개수
URL : https://school.programmers.co.kr/learn/courses/30/lessons/120824
'''
def solution(num_list):
    answer = []
    jak_num = 0
    hol_num = 0
    
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            jak_num += 1
        else:
            hol_num += 1
    
    answer.append(jak_num)
    answer.append(hol_num)
    
    return answer