# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 요약: 정수 n이 어떤 정수 x의 제곱수인지 확인


# ================================================================
# 내 풀이

def solution(n):
    x = int(n ** 0.5)
    
    if x ** 2 == n:
        return (x+1) ** 2
    else:
        return -1
  
# ================================================================
# 다른 풀이

def solution(n):
    x = n ** 0.5
    
    if x % 1 == 0:
        return (x+1) ** 2
    else:
        return -1
