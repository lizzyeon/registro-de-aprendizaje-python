# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12917
# 요약: 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴(Zbcdefg -> gfedcbZ)


# ================================================================
# 내 풀이

def solution(s):
    s = sorted(s, key=str.lower)
    a = 0
    for i in s:
        a += i
        
    return a
# ----------------------------------------------------------------
# s를 1. 대소문자 상관 없이, 2. 오름차순 리스트로 변환하여
# 3. for문으로 문자를 하나씩 붙이면 된다고 생각함
# 하지만, 문자는 +로 붙일 수가 없음 -> ''.join() 사용

# 그리고, 큰 것부터 작은 순은 '내림차순'임 (reverse=True)

# ================================================================
# 수정 풀이

def solution(s):
    return ''.join(sorted(s, reverse = True))
