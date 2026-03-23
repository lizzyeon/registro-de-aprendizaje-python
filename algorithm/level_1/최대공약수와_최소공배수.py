# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12940
# 요약: 두 수의 최대공약수와 최소공배수 구하


# ================================================================
# 내 풀이

def solution(n, m):
    k % n == 0;
    k % m == 0;
  
    return [min(k), n * m / min(k)]
# ----------------------------------------------------------------
# k가 정의되지 않았고, 최소공배수라는 뜻으로 min을 사용하려 했으나 불가

  
# ================================================================
# 다른 풀이

def solution(n, m):
  def gcd(a, b):                   # ★ 유클리드 호제법
      while b != 0:
          a, b = b, a % b
      return a    
  
  return [gcd(n, m), n * m // gcd(n, m)] 

# ================================================================
# ★ 다른 풀이

import math

def solution(n, m):
    g = math.gcd(n, m)
    return [g, n * m // g]

