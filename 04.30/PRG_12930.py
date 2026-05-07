'''
[프로그래머스 Phase1 다루기]

프로그래머스 12930: 이상한 문자 만들기
URL : https://school.programmers.co.kr/learn/courses/30/lessons/12930
'''
def solution(s):
    '''
    구조는 이런식으로 생각 중임.
    일단 s 에서 s.split() 으로 공백 기준으로 단어를 나누면 공백 기준으로 짤린 단어들이 리스트에 들어감
    이제 리스트 형식으로 되었으니 '리스트 컴프리헨션' 으로 접근하면 좋을 것 같은데
    [n for n in range(?)] 형식으로 각 단어들을 뽑은 다음에 뽑은 단어를 또 한글자 알파벳 형식으로 뽑고
    짝수 판별식으로 % 2 == 0 이면 얘를 upper() 치고, % 2 != 0 이면 그냥 기존 문자 그대로 출력한 걸 return 해 줄 변수에     할당하면 될 것 같은데..
    '''
    
    '''
    피드백 1. zip 이 두배열을 묶어서 꺼내주는 도구였다면, enumerate() 는 배열의 "인덱스" 와 "값"을 동시에 꺼내주는 도구
    따라서 for i, char in enumrate("hello") 식으로 진행하면 i 에는 0,1,2 가 char 에는 'h','e','l'... 식으로 꺼내     지게된다.
    
    피드백 2. "삼항 연산자" 라는 개념이 투입되어야 한다. 이 케이스는 보통 c.upper() if i % 2 == 0 else c.lower()
    형태로 연산자를 한 줄에 나열 할 수 있다.
    '''
    
    # 따라서 피드백 받은 부분으로 return 값을 구성하면 다음과 같다.
    return " ".join("".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)) for word in s.split(" "))