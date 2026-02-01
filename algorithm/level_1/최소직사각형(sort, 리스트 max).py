# URL: https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 요약: 4가지의 명함을 수납할 수 있는 가장 작은 지갑의 크기 return
# 예시: [[60, 50], [30, 70], [60, 30], [80, 40]] -> 4000


# ================================================================
# 내 풀이

def solution(s):
    w = max(s)
    h = min(s)
    return max(w)*max(h)

''' ----------------------------------------------------------------
s개의 s 중, w와 h에 상관 없이 큰 값을 꺼내고 4개의 s중 큰 것들 삭제, 
남은 4개의  중 가장 큰 값을 꺼내고 싶은데 그냥 각각 w와 h의 가장 큰 수들이 꺼내졌네..

#1. 그럼, s = [w, h]의 형태에서 우선 w와 h 중 큰 것을 왼쪽에 두면 좋겠다
-> 각 리스트를 내림차순으로 정리.

for card in s:
    card.sort(reverse=True)

#2. 그리고 큰것 중 큰것과, 작은 것 중 큰 것을 곱한다

max(card[0] for card in s)*max(card[1] for card in s)


''' ================================================================
# 완성 풀이

def solution(s):
    
    for card in s:
        card.sort(reverse=True)
        
    return max(card[0] for card in s) * max(card[1] for card in s)


# ================================================================
# 더 간단히 풀이

def solution(s):
    
    return max(max(card) for card in s) * max(min(card) for card in s)
    
# ----------------------------------------------------------------
card의 w와 h을 내림차순 할 필요 없이, max(card)를 통해 원소 중 큰 것 뽑을 수 있음




