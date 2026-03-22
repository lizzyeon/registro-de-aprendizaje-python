# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12950
# 요약: 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열 값 더하


# ================================================================
# 내 풀이

def solution(arr1, arr2):
    for a, b in zip(arr1, arr2):
        answer += [arr1[a] + arr2[b]]
    
    return answer
# ----------------------------------------------------------------
# 이중 행렬이라는 점을 생각하지 않았다
# zip(a, b) = (a[0], b[0]), (a[1], b[1]), (a[2], b[2]), ...


# ================================================================
# 수정 풀이

def solution(arr1, arr2):                      # arr1 = [[1, 2], [3, 4]], arr2 = [[5, 6], [7, 8]]
    result = []                                #        row1[0], row1[1]         row2[0], row2[1]
    
    for row1, row2 in zip(arr1, arr2):         # row1, row2 = ([1, 2], [5, 6]),
        row = []                               # row1, row2 = ([3, 4], [7, 8])

        for a, b in zip(row1, row2):           # zip([1, 2], [5, 6]), zip([3, 4], [7, 8])
                                               #        a       b            a       b    
             row.append(a + b)                 #     [1+5, 2+6],          [3+7, 4+8]
                                               #     [6, 8],              [10, 12]
        result.append(row)                     #     [[6, 8], [10, 12]]
    
    return result

# ----------------------------------------------------------------
# zip이 어려웠다.. zip(a, b)면a와 b에서 하나씩 꺼낸다.


# ================================================================
# 간단히 수정

def solution(arr1, arr2):
    return [[a+b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
    
