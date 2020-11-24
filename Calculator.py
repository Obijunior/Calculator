def int_calculator() :
    num1 = int(input("First number : "))
    Operator = input("Operator(+[addidion]  *[multiplicaton]  /[division]  -[subtraction]  **[square]) : ")
    num2 = int(input("Second number : "))

    if Operator == "+" :
        answer = num1+num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "-" :
        answer = num1 - num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "*" :
        answer = num1*num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "/" :
        answer = num1/num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "**" :
        answer = num1**num2
        print('The answer is ' + str(answer) + '.')

    else :
        print("Error. The opperator you selected was invalid. Please try again")
        calculator()

def flt_calculator():
    num1 = float(input("First number : "))
    Operator = input("Operator(+[addidion]  *[multiplicaton]  /[division]  -[subtraction]  **[square])  sqrt[square root] : ")
    num2 = float(input("Second number : "))

    if Operator == "+" :
        answer = num1+num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "-" :
        answer = num1 - num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "*" :
        answer = num1*num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "/" :
        answer = num1/num2
        print('The answer is ' + str(answer) + '.')

    elif Operator == "**" :
        answer = num1**num2
        print('The answer is ' + str(answer) + '.')

    else :
        print("Error. The opperator you selected was invalid. Please try again")
        flt_calculator()

def str_or_flt():
    type = input("Would you like to use an integer[without decimal points] or float calculator[with decimal points]? (i/f)  ")
    if type == "i" :
        int_calculator()

    elif type == "f" :
        flt_calculator()
    
    else :
        print("Error." + str(type) + "is not a supported type of calculator. Please try again.")
        str_or_flt()

str_or_flt()