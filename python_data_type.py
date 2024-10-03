##숫자형
print("========================NUMBER========================")
print("4 + 7     = " + str(4 + 7    )) #덧셈(정수형)
print("2.0 - 4.0 = " + str(2.0 - 4.0)) #뺄셈(소수형)
print("5 * 3.0   = " + str(5 * 3.0  )) #곱셈(소수형)
print("4 / 2     = " + str(4 / 2    )) #나숫셈(무조건 소수형)
print("7 % 3     = " + str(7 % 3    )) #나머지
print("2 ** 3    = " + str(2 ** 3   )) #거듭제곱

print("7 // 2    = " + str(7 // 2   )) #floor division(버림 나눗셈)
print("8 // 3.0  = " + str(8 // 3.0 ))

print("round(3.141592   ) = " + str(round(3.141592  )))#round 함수
print("round(3.141592, 2) = " + str(round(3.141592,2)))

##문자열
print("")
print("========================STRING========================")
print("KIM")
print("SON")
print("I\'m excited to learn Python!!")
print("Love Lee " * 3)
print("영화 '신세계'에서 \"드루와~\"라는 대사가 유행했다.")

#형변환
print("")
print("========================TYPE CONVERSION========================")
print("int(3.8) = " + str(int(3.8)))
print("float(3) = " + str(float(3)))
print("int(\"2\") + int(\"5\") = " + str(int("2") + int("5")))
print("str(2) + str(5) = " + str(str(2) + str(5)))
age = 7
print("I'm " + str(age) + " years old")

#Formatting
print("")
print("========================FORMATTING========================")
year  = 2024
month = 10
day   = 4
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일 입니다.")
print("오늘은 {}년 {}월 {}일 입니다.".format(float(year), month, day))
date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day))
print("저는 {}, {}, {}를 좋아합니다!".format("1", "2", "3") )
print("저는 {1}, {2}, {0}를 좋아합니다!".format("1", "2", "3"))
num1 = 1
num2 = 2
print("{0} / {1}은 {2:.2f}입니다.".format(num1, num2, num1/num2))

#Boolean
print("")
print("========================BOOLEAN========================")
print(True)
print(False)
print("1 < 2 = {}".format(1 < 2))
print("1 > 2 = {}".format(1 > 2))
print("True and True  = {}".format(True  and True))
print("True or True   = {}".format(True  or  True))
print("True or False  = {}".format(True  or  False))
print("False or False = {}".format(False or  False))
print("False and True = {}".format(False or  True))
print("2 > 1 and \"Hello\" == \"Hello\" = {}".format(2 > 1 and "Hello" == "Hello"))
print("not not True = {}".format(not not True))
print(int(2.5) + int(3.8) > int(str(1) + str(2)))
