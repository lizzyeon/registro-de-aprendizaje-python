# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 요약: 자연수 N의 각 자리 숫자의 합 return


# ================================================================
# 내 풀이

def solution(N):
    return sum(int(i) for i in str(N))


# ================================================================
# 다른 풀이

def solution(N):
    return sum(map(int, str(N)))

# ----------------------------------------------------------------
# map(함수, 배열) -> 배열에 있는 걸 함수에 반복 적용
# map(int, "123") -> int("1"), int("2"), int("3") -> 1, 2, 3
