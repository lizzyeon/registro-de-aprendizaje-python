'''
표준 체중을 구하는 프로그램을 작성하시오
* 표준체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

# ===============================================================================
# 내 풀이

def std_weight(height, gender):

  if height[-2:] == "cm":
    height = int(height[:-2]) / 100

  else:
    height = int(height[:-1])

  if gender == "man":                               # print에서 "남자"로 출력해야 함.
    return round(height * height * 22, 2)           # 소수 둘째자리까지 표시

  elif gender == "woman":                           # print에서 "여자"로 출력해야 함.
    return round(height * height * 21, 2)

profile = std_weight(175cm, "man")
print("키 {} 남자의 표준 체중은 {}kg 입니다."format(height, gender))    # format 앞에 점(.).
                                                                       # gender도 입력 받아야 함.


# ===============================================================================
# 수정 풀이

def std_weight(height, gender):

    if height[-2:] == "cm":
        height = int(height[:-2]) / 100
    
    else:
        height = int(height[:-1])

    if gender == "남자":
        return round(height * height * 22, 2)
    elif gender == "여자":
        return round(height * height * 21, 2)
    
height = "175cm"
gender = "남자"
std_weight = std_weight(height, gender)

print("키 {} {}의 표준 체중은 {}kg 입니다.".format(height, gender, std_weight))
