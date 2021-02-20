def MathOperation():
    """
    Purpose:Use the given Value to Addition,Subtraction,Multiplication and Division
    Pre-Conditions: Should we value
    param value: the value to be added
    Post-Conditions:none
    Return:
        :return Addition,Substaction,Multiplication and Division
    """
    num1 = int(input("Enter the First number"))
    num2 = int(input("Enter the Second number"))

    while True:
        inp = input(
            '''
            What you want to do, Press q to Quite
            For addition press a!
            For Substraction press s!: 
            For Division Press d!: 
            For Multiplication Press m!: 
            ''')
        if inp == 'q' or inp == 'Q':
            break

        try:
            if inp == 'a' or inp == 'A':
                print(f"The Addition of two numbers is {num1 + num2}")
            elif inp == 's' or inp == 'S':
                print(f"The Substraction of two numbers is {num1 - num2}")
            elif inp == 'd' or inp == 'D':
                print(f"The Division of two numbers is {num1 / num2}")
            elif inp == 'm' or inp == 'M':
                print(f"The Multiplication of two numbers {num1 * num2}")
        except Exception as e:
            print(f'You have typed the wrong input is {e}')


MathOperation()




