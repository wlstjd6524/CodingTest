'''
[프로그래머스 Phase1 다루기]

프로그래머스 12948: 핸드폰 번호 가리기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12948
'''
def solution(phone_number):
    answer = ''
    
    # 이런식으로 하면 앞 번호는 어떤 번호가 들어와도 길이 만큼 * 처리가 되는데,
    # 뒤에 나머지 4자리를 구하려고 하는데 슬라이싱을 어떻게 가져와야 하는지... 개념이 잘 안잡힘..
    # answer += ('*' * int(len(phone_number) - 4)) + phone_number[-1:-4]
    return '*' * (len(phone_number) - 4) + phone_number[-4:]