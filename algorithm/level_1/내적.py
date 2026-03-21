# URL: https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 요약: a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]


# ================================================================
# 내 풀이

def solution(a, b):
    
    return sum(ai * bi for ai, bi in zip(a, b))

# ----------------------------------------------------------------
  저번 풀이에서 썼던 sum 사용했다! 뿌듯 ^_^
