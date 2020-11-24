def calculator() :
    num1 = int(input("First number : "))
    Operator = input("Operator(+  *  /  -  **[squared]) : ")
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

calculator()