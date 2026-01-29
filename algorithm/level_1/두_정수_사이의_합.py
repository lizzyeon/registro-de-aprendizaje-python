# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 요약: 정수 a와 b 사이에 속한 모든 정수의 합을 return

# ================================================================
# 내 풀이

def solution(a, b):
    n = 0
    
    if a <= b:
        for k in range(a, b+1):
            n += k
    else:
        for k in range(b, a+1):
            n += k
    return n

# ----------------------------------------------------------------
# 맞았는데, 줄여보고 싶다
# if/else를 사용하지 않고, (작은 것, 큰 것+1) 형태로 만들어보자

# ================================================================
# 수정 풀이

def solution(a, b):
    n = min(a, b)
    m = max(a, b)

    return sum(k for k in range(n, m+1))


# ================================================================
# 더 간단한 풀이

def solution(a, b):

    return sum(k for k in range(min(a, b), max(a, b)+1))




# ----------------------------------------------------------------
