# URL: https://school.programmers.co.kr/learn/courses/30/lessons/181906
# 요약: is_prefix가 my_string의 접두사인지 확인


# [시도1] 
# if my_string(string) = is_prefix(string)
#    answer = 1
# else
#    answer = 0
#
# 문법을 몰랐음. 함수끼리 같을 땐 '==' 사용, if와 else에선 뒤에 ':' 붙이기


# [올바른 풀이]
def solution(my_string, is_prefix):
  return int(my_string.startwith(is_prefix))

# A.startwigh(B) : 문자열 A의 앞부분이 B로 시작하나? -> True/False
# my_string.startwith(is_prefix) : my_string의 앞부분이 is_prefix로 시작하나?
# ex) BANANA.startwigh(BAN) -> True

# int 타입 <- bool 타입
# int(True) == 1
# int(False) == 0
