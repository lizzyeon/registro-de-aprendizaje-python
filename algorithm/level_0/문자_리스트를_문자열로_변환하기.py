# URL: https://school.programmers.co.kr/learn/courses/30/lessons/181941
# 요약: (입력) ["a","b","c"] -> (출력) "abc"


# ================================================================
# 내 풀이
def solution(a):
    return ''.join(i for i in a)
  
# ----------------------------------------------------------------
# a는 배열이기 때문에 for문 없이 그냥 a 써도 무방

def solution(a):
    return ''.join(a)
