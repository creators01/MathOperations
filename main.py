def MathOperation(num1,num2):
    """
            Purpose:
                Use the given Value to Addition,Subtraction,Multiplication and Division
            Pre-Conditions:
                :param value: the value to be added
            Post-Conditions:
                none
            Return:
                :return Addition,Substaction,Multiplication and Division
            """
    inp = input('''What you want to do, Press q to Quite
For addition press a!
For Substraction press s!: 
For Division Press d!: 
For Multiplication Press m!: 
''')
    if inp == 'a' or inp == 'A':
            return num1 + num2
    elif inp == 's' or inp == 'S':
            return num1 - num2
    elif inp == 'd' or inp == 'D':
            return num1/num2
    elif inp == 'm' or inp == 'M':
            return num1*num2
    else:
        print("it is not handled by this program")

test1 = MathOperation(5,10)
print(test1)
test2 = MathOperation(0, 0)
print(test2)
test3 = MathOperation(4, 50)
print(test3)






