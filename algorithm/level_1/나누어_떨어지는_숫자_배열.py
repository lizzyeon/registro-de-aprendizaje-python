# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 요약: arr를 divisor로 나눳을 때 나눠 떨어지는 값을 오름차순으로 정렬한 배열 리턴

# ================================================================
# 내 풀이

def solution(arr, divisor):
    
  for i in arr:
      if i % divisor == 0:
          return [i]
# ----------------------------------------------------------------
# for문으로 어떻게 리스트를 만들어야 할까? -> .append()
# 오름차순 -> sorted() or .sort()          
# 내림차순 -> sorted( , reverse=true)

# ================================================================
# 수정 풀이

def solution(arr, divisor):
  answer = []
  
  for i in arr:
    if i % divisor == 0:
      answer.append(i)

    if not answer:
      return [-1]

  return sorted(answer)
          
# ----------------------------------------------------------------
# 간단히 수정

def solution(arr, divisor):
  answer = [i for i in arr if i % divisor == 0]

  return sorted(answer) if answer != [] else [-1]

# ----------------------------------------------------------------
# return sorted(answer) if answer else [-1]
# 이렇게만 해줘도 됨. 'if answer'은 'answer이 비어있지 않으면' 이라는 뜻

# return sorted=(answer) or [-1]
# 이것도 가능. '조건 맞는 값 반환, 없으면 [-1]'

# ----------------------------------------------------------------
return sorted(answer) if answer != [] else [-1]
return sorted(answer) if answer else [-1]
return sorted=(answer) or [-1]


  
