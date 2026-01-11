# URL: https://school.programmers.co.kr/learn/courses/30/lessons/181938
# 요약: (입력) a+b(문자열), 2ab(값) 중 더 큰 값을 리턴 


# ================================================================
# 내 풀이

def solution(a, b):
    return max(int(str(a)+str(b)),2*a*b)
