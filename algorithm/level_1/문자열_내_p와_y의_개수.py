# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12916
# 요약: 문자열 내 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return


# ================================================================
# 내 풀이

def solution(s):
    for i in s:
        if (count(i) = p) = (count(i) = y):
            return True
        else:
            return False
# ----------------------------------------------------------------

#1. =가 아닌 == 사용

#2. count(i) = p     -> s.count('p')   # count()만 단독으로 사용 불

#3. for와 if문의 혼합 사용 
#   -> 문자열 중 하나의 i만을 비교해서 true/false를 찾는다면 사용해도 되지만
#   -> 지금처럼 모든 문자열을 비교해야 한다면 적합하지 않음


# ================================================================
# 완성 풀이

def solution(s):
    s = s.lower()                            # 대소문자 구분없이 비교하기 위해
    return s.count('p') == s.count('y')      # s문자열에 p와 y의 갯수 비교


# ================================================================
# 다른 풀이

def solution(s):
    s = s.lower()
    a = 0
    b = 0

    for i in s:
        if i == 'p':
            a += 1
        elif i == 'y':
            b += 1

    return a == b
