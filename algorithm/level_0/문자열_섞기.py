# URL: https://school.programmers.co.kr/learn/courses/30/lessons/181942
# 요약: (입력) aaaaaa, bbbbbb -> (출력) abababababab 
# 손도 못댐


# ================================================================
# 완성 풀이

def solution(a, b):
    answer = ""
    
    for i in range(len(a)):
        answer += a[i] + b[i]
    return answer

# ----------------------------------------------------------------
# for i in range(len(a)) : a의 문자 수만큼 반복하겠다
# len(a) : 문자열 a의 길이                           # len(aaaa) -> 4 
# range(len(a)) : 0부터 len(a)전까지의 숫자를 만듦   # range(4)  -> 0, 1, 2, 3
# for i in range(len(a)) : a의 문자 수만큼 반복하겠다

# range(10)    -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9  : 0부터 10 전까지의 숫자
# range(2, 10) ->       2, 3, 4, 5, 6, 7, 8, 9  : 2부터 10 전까지의 숫자
# range(2, 10, 3) ->    2,       5,       8     : 2부터 10 전까지, 3씩 증가


# ================================================================
# 다른 풀이

def solution(a, b):
  return ''.join(a1 + b1 for a1, b1 in zip(a, b))

# ----------------------------------------------------------------
# a = "ankle", b = "brown" 이라고 하면 
# zip(a, b) -> ('a', 'b'), ('n', 'r'), ('k', 'o'), ('l', 'w'), ('e', 'n')
# for a1, b1 in zip(a, b) -> a와 b의 문자를 동시에 꺼내서
# a1 + b1 -> 'ab' + 'nr' + 'ko' + 'lw' + 'en' 
# ''.join() : 'abnrkolwen'



