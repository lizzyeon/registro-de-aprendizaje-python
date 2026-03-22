# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 요약: 배열 중 중복된 원소는 제외하고 리턴


# ================================================================
# 내 풀이

def solution(arr):
    answer=[]
    for i in range(len(arr)):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    
    return answer        
# ----------------------------------------------------------------
# arr = [3, 4, 5]일 때, i = 0, 1, 2
# 이때 i=2라면, 'if arr[2] != arr[3]:'은 불가. 왜냐하면 arr[3]은 없음
# 따라서 숫자 조정 필요


# ================================================================
# 수정 풀이

def solution(arr):
  answer=[arr[0]]
  for i in range(1, len(arr)):
      if arr[i] != arr[i-1]:
          answer.append(arr[i])
  
  return answer        


# ================================================================
# ★ 다른 풀이

from itertools import groupby

def solution(arr):
    return [k for k, _ in groupby(arr)]

# ----------------------------------------------------------------
# arr = [1,1,1,3,3,0,1,1]
# groupby : 연속된 값들을 묶어준다
# for a, b in groupby(arr) : a, b = 1, (1,1,1) / 3, (3,3) / 0, (0) / 1, (1,1)

# k for k, _ in groupby(arr) : 1, 3, 0, 1




