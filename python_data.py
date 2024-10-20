#list
numbers = [1,2,3,4,5,6,7,8,9]
names = ["Kim", "Lee", "Son", "Park"]

print(numbers)
print(names)

#list indexing
print(names[1]) # "Lee"
print(numbers[0] + numbers[3]) #5
#print(numbers[4]) #IndexError: list index out of range
print(numbers[-1]) #4
print(numbers[-2]) #3

#list slicing
print("\n List Slicing")
print(numbers[0:4]) #0~3index 까지 잘라서 사용
print(numbers[:3] ) #0~2index 까지 잘라서 사용  
new_list = numbers[:3]
print(new_list[1:]) #1~마지막 index 까지 사용

#list 접근
print("\n List Element")
numbers[0] = numbers[0] + numbers[5]
print(numbers[0]) #7

#list function
print("\n List 추가")
numbers2 = []
print(len(numbers2)) #0
numbers2.append(5) #[5]
numbers2.append(8) #[5, 8]
print(numbers2)

print("\n List Element Delete or Insert")
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8]
del numbers3[3] #3index element 삭제 -> [1, 2, 3, 5, 6, 7, 8]
print(numbers3)
numbers3.insert(3, 44) #3index element에 추가 -> [1, 2, 3, 44, 5, 6, 7, 8]
print(numbers3)


#list sorting
print("\n List Sorted")
numbers4 = [19, 13, 2, 5, 3, 11, 7, 17]
new_numbers4 = sorted(numbers4) #오름차순 정렬
print(new_numbers4) #[2, 3, 5, 7, 11, 13, 17, 19]
new_numbers4 = sorted(numbers4, reverse=True) #내림차순 정렬
print(new_numbers4) #[19, 17, 13, 11, 7, 5, 3, 2]
print(numbers4) #기존 리스트는 정렬 되지 않음!

print("\n List Sort")
print(numbers4.sort()) #list자체를 정렬
print(numbers4)

#list exercise1
# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 여기에 코드를 작성하세요
    idx = 0
    c_list = []
    while idx < len(fahrenheit) :
        c = round(((fahrenheit[idx] - 32) * 5) / 9, 2)
        c_list.append(c)
        idx += 1
    return c_list

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요
another = fahrenheit_to_celsius(temperature_list)
print("섭씨 온도 리스트: {}".format(another))  # 섭씨 온도 출력

#list exercise2
# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    # 여기에 코드를 작성하세요
    return krw / 1000

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    # 여기에 코드를 작성하세요
    return usd * (1000 / 8)

# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# prices를 원화(￦)에서 달러($)로 변환하기
# 여기에 코드를 작성하세요

# 달러($)로 각각 얼마인가요?
idx = 0
while idx < len(prices) :
    prices[idx] = krw_to_usd(prices[idx])
    idx += 1
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
# 여기에 코드를 작성하세요
idx = 0
while idx < len(prices) :
    prices[idx] = usd_to_jpy(prices[idx])
    idx += 1
# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))

#list function exercise1
# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
# 코드를 입력하세요
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
idx = 0
while idx < len(numbers) :
    if numbers[idx] % 2 == 1 :
        del numbers[idx]
    else :
        idx += 1
print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
numbers.sort()
print(numbers)



#for loop
print("\n for loop with range parameter 2")
start = 3
stop = 11
step = 2
for i in range(start, stop) : 
    print(i)

print("\n for loop with range parameter 1")
for i in range(stop) : 
    print(i)

print("\n for loop with range parameter 3")
for i in range(start, stop, step) : 
    print(i)

# for exercise1
print("\n for exercise1")
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#for i in numbers : 
#    print("{} {}".format(numbers.index(i),i))
for i in range(len(numbers)) : 
    print(i, numbers[i])

# for exercise2
print("\n for exercise2")
for i in range(11) : 
    print("2^{} = {}".format(i, 2 ** i))


# for exercise3
print("\n for exercise3 구구단")
for i in range(1, 10) : 
    for j in range(1, 10) : 
        print("{} * {} = {}".format(i,j,i*j)) 

# for exercise4
print("\n for exercise4 피타고라스3조")
#a^2 + b^2 = c^2을 지키고, a+b+c = 400, a<b<c조건 지키는 값의 a*b*c값
for a in range(1, 401) : 
    a_square = a * a 
    for b in range(a, 401) :
        b_square = b * b
        c = 400 - a - b
        if a_square + b_square == c * c and b < c : 
            print(a, b, c)
            print(a * b * c)
        
# for exercise5
print("\n for exercise5 list 뒤집기")        
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
#numbers.reverse()
for left_idx in range(len(numbers) // 2) :
    right_idx = len(numbers) - left_idx - 1

    temp = numbers[left_idx]
    numbers[left_idx] = numbers[right_idx]
    numbers[right_idx] = temp
print("뒤집어진 리스트: " + str(numbers))