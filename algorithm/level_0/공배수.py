# URL: https://school.programmers.co.kr/learn/courses/30/lessons/181936
# 요약: a가 n과 m의 공배수이면 1, 아니면 0 리턴

# ================================================================
# 내 풀이

def solution(a, n, m):
    
    if a%n == 0 and a%m == 0:
         return 1
    else:
        return 0

# ----------------------------------------------------------------
# 간단히 ver.

def solution(a, n, m):
    return 1 if a % n == 0 and a % m == 0 else 0


# ----------------------------------------------------------------
# 다른 ver. (bool -> int)

def solution(a, n, m):
    return int(a % n == 0 and a % m == 0)
