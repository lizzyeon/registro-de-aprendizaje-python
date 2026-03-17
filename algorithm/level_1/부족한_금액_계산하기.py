# URL: https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 요약: money원 만큼의 돈을 들고 price원의 놀이기구를 count만큼 타려고 할 때 모자란 금


# ================================================================
# 내 풀이

def solution(price, money, count):
    a = 0
    for i in range(1,count+1):
        a += price * i
    
    if a > money:
        return a - money 
    else:
        return 0
  
# ================================================================
# 다른 풀이 ★

def solution(price, money, count):
    total = price * (count * (count + 1) // 2)
    return max(0, total - money)

# for문보다 처리가 빠름
# if 조건문 없이 처리
# '//'로 나누면 int가 됨 (12 / 2 = 6.0, 12 // 2 = 6)


