# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 요약: 문자열 s의 길이가 4 또는 6이고, 숫자로만 구성돼있는지 확인


# ================================================================
# 좋은 풀이

def solution(s):
    return len(s) in [4, 6] and s.isdigit()
  
# ----------------------------------------------------------------
# return은 자동으로 참이면 True, 거짓이면 False를 반환한다.
# ★ len(s) in [4, 6] : len(s)의 길이가 4 또는 6인지 확인
# ★ .isdigit() : 숫자만 / .isalpha() : 문자만 / .isalnum() : 숫자+문자

  
# ================================================================
# 나쁜 풀이

def solution(s):
    try:
        int(s)
        return len(s) == 4 or len(s) == 6
    except:
        return False

# ----------------------------------------------------------------
# try: except: : 일단 try해보고 에러나면 except 반환 
# 예외를 사용하면 비효율적임. 쓸데없이 무겁다.
