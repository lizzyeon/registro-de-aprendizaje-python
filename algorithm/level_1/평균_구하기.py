# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 요약: 배열의 평균 값을 return


# ================================================================
# 내 풀이

def solution(arr):
    return sum(map(int, arr))/len(arr)
  

# ================================================================
# 다른 풀이

def solution(arr):
    return sum(arr)/len(arr)
  
# 배열함수의 원소들은 그냥 sum으로 다 더할 수 있다!!
