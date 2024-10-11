import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

calc_funcs = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def new_calc():
    first_num = int(input("What is your first number?\n"))
    operator = input("What would you like to do with this number? +, -, *, /\n")
    second_num = int(input("What is your second number?\n"))
    return calc_funcs[operator](first_num, second_num)

def cont_calc(first_number):
    operator = input("What would you like to do with this number? +, -, *, /\n")
    second_num = int(input("What is your second number?\n"))
    return calc_funcs[operator](first_number, second_num)

def calculator():
    print(art.logo)
    output = new_calc()
    looping = True
    while looping:
        if input(f"The result is {output}, would you like to keep working with this number?") == "yes":
            output = cont_calc(output)
            looping = True
        else:
            looping = False
            calculator()
            print("\n" * 30)

calculator()