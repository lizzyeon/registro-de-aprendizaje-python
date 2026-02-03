# URL: https://school.programmers.co.kr/learn/courses/30/lessons/42840


# ================================================================
# 내 풀이

def solution(a):
    x = [1, 2, 3, 4, 5] * 2000
    y = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    p = 0
    q = 0
    r = 0
    
    for i in a:
        if x.(a.index(i)) = a.index(i):       # a = [1, 3, 2, 4, 3]일 때
            p += 1                            # a.index(3)는 항상 1만 return
        if y.(a.index(i)) = a.index(i):       # 4에 있는 3까지 가지 못함
            q += 1
        if z.(a.index(i)) = a.index(i):       # 문법적으로 맞지 않음. 대폭수정
            r += 1

    if max(x, y, z) = x:                      # x, y, x를 비교할게 아니라
        return [1]                            # p, q, r (맞힌 개수)를 비교해야 함
    elif max(x, y, z) = y:
        return [2]
    else:
        return [3]


# ================================================================
# 수정 풀이

def solution(a):
    x = [1, 2, 3, 4, 5] * 2000
    y = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    z = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    p = q = r = 0

    for i in range(len(a)):            
        if a[i] == x[i]:         # a(답)과 x의 답을 맞춰보기
            p += 1               # 맞으면 +1점
        if a[i] == y[i]:
            q += 1
        if a[i] == z[i]:
            r += 1

    scores = [p, q, r]
    max_score = max(scores)

   return [i + 1 for i in range(3) if scores[i] == max_score]

'''
for i in range(3)                 0(p), 1(q), 2(r) 인덱스값 중 
if scores[i] == max_score         최고점과 같은 점수인 사람을
i + 1                             i+1로 표현


''' ================================================================
# 다른 풀이

def solution(a):
  patterns = [                          
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  ]

  scores = [0, 0, 0]

  for i in range(len(a)):
    for j in range(3):
    if a[i] == patterns[j][i % len(patterns[j])]:
      scores[j] +=1

  max_score = max(scores)

  return [i+1 for in range(3) if scores[i] == max_score]

''' ----------------------------------------------------------------

1. patterns 에 수포자 1, 2, 3의 패턴을 입력한다. 그리고 이후에 반복되도록 함수를 설정한다
   ex) pattern[0] = [1, 2, 3, 4, 5]

2. for i in range(len(a)):                          -> 문제번호 0번부터의 답 순회
   for j in range(3):                               -> 3명의 수포자들 검사

3. if a[i] == patterns[j][i % len(patterns[j])]:

  patterns[j]  : j번 수포자의 답 패턴
  i % len(patterns[j]) : 패턴을 반복하도록
  patterns[j][i % len(patterns[j])] : j번 수포자가 i번째 문제에서 고른 답
  * patterns[j][3] : j번 수포자의 3번 답을 꺼내라(곱하기 아님)
  a[i] == patterns[j][i % len(patterns[j])] : 실제 정답과 수포자의 답이 같은지 비교
  
  '''
