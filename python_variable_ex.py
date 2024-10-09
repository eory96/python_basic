#python varialbe exercise
def first():
    message = "Hello"
    return message

def second():
    message = "Hi"
    print(message)

def third():
    message = None

print(first())
second()
print(third())
print(third())

#python optional parameter
def myself(name, age, nationality = "South Korea"):
    print("My name is {}".format(name))
    print("My age is {}".format(age))
    print("My nationality is {}".format(nationality))

myself("Kim", 29)
print()
myself("Tom", 20, "America")

#python variable scope
def my_func():
    x = 3
    print(x)

my_func()
#print(x) #error 출력 x는 my_func안에서만 유효하다.

y = 2
def my_func2():
    print(y)

my_func2()  #2
print(y)    #2

z = 5
def my_func3():
    z = 3
    print(z)

my_func3() #3
print(z)   #5

#constants
PI = 3.14 #기본적은 변수 정의와는 별 차이 없지만 변하지 않는 값(상수)에 대해서는 대문자로 정의(#define과 같은 용도)

def circle_area(r):
    area = PI * r * r
    print("반지름은 {}면, 넓이는 {}".format(r, area))

radius = 4
circle_area(radius)
radius = 6
circle_area(radius)

#exercise1 - even?odd?
def is_evenly_divisible(number):
    return number%2 == 0

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))

#exercise2 - exchage
def calculate_change(payment, cost):
    #remain_money = payment - cost

    #money_50000 = int(remain_money / 50000)
    #remain_money -= money_50000 * 50000
    #print("50000원 지폐: {}장".format(money_50000))

    #money_10000 = int(remain_money / 10000)
    #remain_money -= money_10000 * 10000
    #print("10000원 지폐: {}장".format(money_10000))
    
    #money_5000 = int(remain_money / 5000) 
    #remain_money -= money_5000 * 5000
    #print("5000원 지폐: {}장".format(money_5000))

    #money_1000 = int(remain_money / 1000) 
    #print("1000원 지폐: {}장".format(money_1000))
    change = payment - cost
    fifty_count = change // 50000
    ten_count   = (change % 50000) // 10000
    five_count  = (change % 10000) // 50000
    one_count   = (change % 5000) // 1000     

    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))
    
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)    