import random
import math
import string

# This function open's/read's up a password file (I need to find a way to iterate through the list
# so that different passwords may be inserted.

try:
    password_file = open('/media/lunga/LUNGA/PycharmProjects/automate_boring_stuff/SecretPasswordFile.txt')
    secret_password = password_file.read()

    # This requests the user to insert their credentials
    print('Please enter your password')
    typed_pass = input()

    # Verifies what is typed against what is in the file that was read in line 8
    if typed_pass == secret_password:
        print('Access granted !!!\n\n')
    else:
        print('Incorrect password. So, "Access Denied!!!"\n\n')
    


    # I will execute the greeting function here
    def calc():
        # This is is the welcome text
        print('''Welcome to Lunga Mthombothi's simple calculator simulator.\nWhere you will input two numbers,\nthen insert the symbol you wish to compute the two numbers with.\n
         ''')
        # I then request input from the user...however, this would need to be in
        # an integer format. I need to find a way to throw my own error that
        # keeps the flow control within the program
        num_1 = int(input('Faka iNumba yoku qala: '))
        num_2 = int(input('faka iNumba yesi bili: '))

        # This requests the user to insert a mathematical symbol for simple calculation. The current
        # options are (plus, minus, multiply and divide)
        operation_var = input('''
                    Please enter your mathematical elements you want to calculate with this calculator program:
                    + for addition
                    - for subtraction
                    * for multiplication
                    / for division
                    % for Modulus
                    ''')
        # In this block
        if operation_var == '+':
            print('{} + {} ='.format(num_1, num_2))
            print('Impendulo yakho: \n', num_1 + num_2)
        elif operation_var == '-':
            print('{} - {} ='.format(num_1, num_2))
            print('Impendulo yakho: \n', num_1 - num_2)
        elif operation_var == '*':
            print('{} * {} ='.format(num_1, num_2))
            print('Impendulo yakho: \n', num_1 * num_2)
        elif operation_var == '/':
            print('{} / {} ='.format(num_1, num_2))
            print('Impendulo yakho: \n', num_1 / num_2)
        elif operation_var == '%':
            print('{} / {} ='.format(num_1, num_2))
            print('Impendulo yakho: \n', num_1 / num_2)
        else:
            print('Error! Invalid operation conducted!!! Please run program and try again with correct parameters!!!')


    calc()


    def play_again():
        calc_again = input('''Ufuna ukubala futhi?
        uY for uYebo noma uQ for uQha!
    ''')

        while calc_again.upper() == 'Y':
            return calc()
            return play_again()

        if calc_again.upper() == 'Q':
            return print('Hamba Kahle :) ')


    play_again()
except ZeroDivisionError:
    print("Error! Please note that you cannot divide a number by Zero (0)")
    

