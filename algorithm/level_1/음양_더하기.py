# URL: https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 요약: [4, 7, 12] & [true, false, true] -> +4 -7 +12 = 9


# ================================================================
# 내 풀이

def solution(absolutes, signs):
    answer = 0
    for a, b in absolutes, signs:
        answer += a * b
    
    return answer
# ----------------------------------------------------------------
# 1. 두 리스트에서 각각의 변수를 뽑으려면 zip()으로 묶어줘야 함
# 2. true와 false는 자동으로 1과 0으로 계산되지 않음

  
# ================================================================
# 수정 풀이

def solution(absolutes, signs):
  answer = 0
  for a, b in zip(absolutes, signs):
      if b:
          answer += a
      else:
          answer -= a
  
  return answer

# ----------------------------------------------------------------
# ★ 더 간단히 풀이

def solution(absolutes, signs):
    return sum(a if b else -a for a, b in zip(absolutes, signs))

# 스고이,, 더한다고 해서 'answer +='만 생각하지 말자!


    
