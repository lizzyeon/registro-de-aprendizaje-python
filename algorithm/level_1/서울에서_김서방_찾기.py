# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 요약: string 배열 seoul의 요소 중 'Kim'의 위치 x를 찾아 '김서방은 x에 있다'는 string 반


# ================================================================
# 정답 풀이

def solution(seoul):
  return "김서방은 {}에 있다".format(seoul.index('Kim'))

# ----------------------------------------------------------------

# {}.format() : {}에 () 값이 들어감 
# "김서방은 {}에 있다".format(1)    -> "김서방은 1에 있다"

# seoul.index('???')                 -> seoul이라는 리스트에서 ???값이 처음 등장하는 위치(index)를 반환
# seoul = [ "ㅎㅎㅎ", "ㅇㅇㅇ", "???"]
# seoul.index('???')                 -> 결과 : 2 (0부터 시작)


# ================================================================
# 다른 풀이

def solution(seoul):
  return f"김서방은 {seoul.index('Kim')}에 있다"
  
# ----------------------------------------------------------------

#   return "김서방은 {}에 있다".format(seoul.index('Kim'))
#   return f"김서방은 {seoul.index('Kim')}에 있다"
#   두 개가 같은 결과임.
