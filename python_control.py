#while loop
i = 1
while i <= 3:
    print("I'm handsome!!")
    i += 1

even = 2
while even <= 100:
    print(even)
    even+=2

NUM_23 = 23
multiple_value = 1
result = NUM_23 * multiple_value

is_hundred_under = True
while result < 100 :
    result = NUM_23 * multiple_value
    multiple_value += 1

print(result)

#if
TEMPERATURE_STANDARD = 10
temperature = 10
if temperature <= TEMPERATURE_STANDARD:
    print("Put on a jacket!!")
else :
    print("Don't have to take out a jacket")

#elif exersice1
def print_grade(midterm_score, final_score):
    total_score = midterm_score + final_score
    if total_score >= 90:
        print("A")
    elif total_score >= 80 and total_score < 90:
        print("B")
    elif total_score >= 70 and total_score < 80:
        print("C")
    elif total_score >= 60 and total_score < 70:
        print("D")
    else :
        print("F")

print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)        