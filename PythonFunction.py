def say_hello():
    print("Hello World!")
say_hello()#Always call a funtion to that it will excute
say_hello()


#Function with a single parameter
def greet(name):
    print("Hello " + name + "!")

greet("Odwa")

#Function with 2 parameter
def greet_two(name_one, name_two):
    print("Hello " + name_one + " and " + name_two)
greet_two("Odwa", "Nokwanda")


#Function with 3 parameter mathematical calculation
def  calc_total(amount, terms, interest):
    total = amount + interest * amount * terms
    return total

total = calc_total(1000, 5, 0.1)
print(total)

#The abirtrary Arguments *args if you not sure how parameter you put in a function
def gree_p(greeting, **names):#Two **arg will give dictionary
    for n in names:
        print(greeting + n)

gree_p("Hi! Welcome ",  s="Odwa" , j="Thandi")

###############################################################Exercise 1 Functions


def distance_from_zero(num):
    if type(num) is int or type(num) is float:
        num = abs(num)
        return True
    else:
        return "Nope"

print(distance_from_zero(5))
print(distance_from_zero(5.5))
print(distance_from_zero("grfdn"))

#################################################################Exercise 2 Functions

def is_leap_year():
    year = int(input("Please Enter a Year: "))

    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 400 ==0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is not a Leap Year")
    else:
        print(year, "is not a Leap Year")


is_leap_year()



