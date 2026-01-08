# URL: https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 요약 : index_list에 있는 인덱스를 이용해 my_string에서 문자 추출하여 순서대로 합치기
# 손도 못댔다... 여러가지 풀이법을 분석해보자


#==============================================================================================
# 1
def solution(my_string, index_list):
  answer = ""                            # 문자열을 합칠 때 초기값이 꼭 필요하다. 빈 문자열 생성
  for i in index_list:                   # index_list에 들어 있는 값을 앞에서부터 하나씩 꺼냄
    answer += my_string[i]               # answer = answer + my_string[i] 와 같음. 기존 answerdp에 새 문자 붙이
  return answer                          # └ my_string[i] : i번째 글자 (0부터 시작)

#-----------------------------------------------------------------------------------------------
# 예시
# my_stirng = zpiaz, index_list = [1,2,0,4,3]
# index_list의 0번째 숫자인 1 -> my_string[1] (1번 문자를 꺼내라) -> p
# index_list의 1번째 숫자인 2 -> my_string[2] (2번 문자를 꺼내라) -> i
# index_list의 2번째 숫자인 0 -> my_string[0] (0번 문자를 꺼내라) -> z
# index_list의 3번째 숫자인 4 -> my_string[4] (4번 문자를 꺼내라) -> z
# index_list의 4번째 숫자인 3 -> my_string[3] (3번 문자를 꺼내라) -> a


#===============================================================================================
# 2 (업그레이드)
def solution(my_string, index_list):
  return ''.join(my_string[i] for i in index_list)
                 
#-----------------------------------------------------------------------------------------------
# ''.join() : () 안의 문자열을 구분자로 이어 붙여라
# <ex>  ''.join([a,b,c]) : abc    -> '' 안에 문자 없으므로 구분자 없음
# <ex> '-'.join([a,b,c]) : a-b-c  -> '-' 구분자로 구분

                 
