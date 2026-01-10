# URL: https://school.programmers.co.kr/learn/courses/30/lessons/181944
# 요약: (입력) 짝수/홀수 -> (출력) '짝수/홀수 is even/odd'


# ================================================================
# 내 풀이

a = int(input())
if a%2 == 0:
    print(a, 'is even')
    
else:
    print(a, 'is odd')


# ================================================================
# 다른 풀이

a = int(input())
print(f'{a} is {'even' if a % 2 == 0 else 'odd'}')

# ----------------------------------------------------------------
# print(f'{a} is {}') 형태로 시작. a에 따라 even이나 odd가 들어감
# 'even' if a % 2 == 0 else 'odd'     <- if else 한 줄에 쓰는 방법

# 'odd' if a % 2 else 'even' 도 가능
# if 뒤 조건문이 true이면 odd, false이면 even
# 파이썬에선 정수를, 0이 아닌 수는 true, 0은 false로 평가함
# 이때 a가 홀수이면 'a % 2 != 0' 이므로 true
# 이때 a가 짝수이면 'a % 2 == 0' 이므로 false
# 좀 헷갈리네.. 0이 false!!
