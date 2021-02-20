def MathOperation(num1,num2):
    """
            Purpose:
                Use the given Value to Addition and Subtaction
            Pre-Conditions:
                :param value: the value to be added
            Post-Conditions:
                none
            Return:
                :return Addition or Substaction
            """
    inp = input('''What you want to do, For addition press a! For Substraction press s!: ''')
    if inp == 'a' or inp == 'A':
        return num1 + num2
    elif inp == 's' or inp == 'S':
        return num1 - num2
test1 = MathOperation(5,10)
print(test1)

