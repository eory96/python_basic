#basic of python function
def hello():
    print("Hello")
    print("World!!")

hello()

def recipeOfCafeMoca():
    print("1. 준비된 컵에 초코 소스를 넣는다.")
    print("2. 에스프레소를 추출하고 잔에 부어 준다.")
    print("3. 초코 소스와 커피를 잘 섞어 준다.")
    print("4. 거품기로 우유 거품을 내고, 잔에 부어 준다.")
    print("5. 생크림을 얹어 준다.")

recipeOfCafeMoca()
recipeOfCafeMoca()

#functino parameter
def hello_parameter(name, age):
    print("Hello")
    print(name)
    print("age : " + str(age))

hello_parameter("Son", 29)