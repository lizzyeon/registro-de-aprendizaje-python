# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 요약: n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴


# ================================================================
# 내 풀이

def solution(n):
    return ''.join(sorted(str(n), reverse = True))

# ----------------------------------------------------------------
# sorted(리스트 또는 배열, reverse = True) -> 내림차순 함
# 그런데 반환되는 값이 여전히 Str임. 숫자로 바꿔줘야 함


# ================================================================
# 완성 풀이

def solution(n):
    return int(''.join(sorted(str(n), reverse = True)))
