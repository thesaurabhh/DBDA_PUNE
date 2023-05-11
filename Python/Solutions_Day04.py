
# Solution to Practice problem 1 in loops_demo.py

# """
# if the number is divisible by 3 print Fizz    
# if the number is divisible by 5 print Buzz
# if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

# Testcase : 
#     21 --> Fizz
#     50 --> Buzz
#     15 --> Fizz Buzz
#     22 --> Invalid Input 
# """

# num = int(input("Please enter the number"))

# """
# if num %5==0 and num % 3 ==0 :
#     print("Fizz Buzz")
# elif num%3 == 0 :
#     print("Fizz")
# elif num%5 == 0 :
#     print("Buzz")
# else:
#     print("Invalid Input")
    


# if num %5==0  :
#     if num % 3 ==0 : 
#         print("Fizz Buzz")
#     else:
#         print("Buzz")    
# elif num%3 == 0 :
#     print("Fizz")
# else:
#     print("Invalid Input")
    
# """
# # very specific to python
# is_inside_if_clause = 'N'
# if num%3 == 0 :
#     print("Fizz",end = ' ' )
#     is_inside_if_clause = 'Y'

# if num%5 == 0 :
#     print("Buzz")
#     is_inside_if_clause = 'Y'

# if  is_inside_if_clause != 'Y':
#     print("Invalid Input")


#*****************************************
# """Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game"""
# def fizz_buzz():
#     num = int(input("Please enter a number"))
#     is_inside_if_clause = 'N'
#     if num%3 == 0 :
#         print("Fizz",end = ' ' )
#         is_inside_if_clause = 'Y'

#     if num%5 == 0 :
#         print("Buzz")
#         is_inside_if_clause = 'Y'

#     if  is_inside_if_clause != 'Y':
#         print("Invalid Input")


# def play_game():
#     while(True):
#         print("Lets Play Fizz Buzz   !!!! ")
#         fizz_buzz()	
#         choice = input("\n Do you want to continue (Y/N)").lower()     
#         if choice == 'n':
#             break

# # function calls
# play_game()  


#******************** Assignment ************************

"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
"""

#Solution to above assignment:

from function_definitions import *
def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_addition(first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        returned_value = my_square(first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        returned_value = my_exponenation(first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

def iterative_calculator():
    while(True):
        print("Lets start   !!!! ")
        my_calculator()	
        choice = input("\n Do you want to continue (Y/N)").lower()     
        if choice == 'n':
            break

iterative_calculator()    