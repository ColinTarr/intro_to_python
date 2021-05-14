greeting = "Hello there young one. Welcom to Narnia. What is your name?"


def the_intro():
    print(greeting)
    char_name = input("Please enter your name: ")
    welcome_greeting = print("It is nice to have you here " + char_name + ". Walk with me as I tell you a story.")

the_intro()

def math_addition():
    x = float(input("Please enter the first number to add: "))
    y = float(input("Please enter the second number to add: "))
    z = x + y
    print(f"x + y = {z}")
    print(type(z))

math_addition()