"""
--------------------
Exercise 
-------------------
Lets implement my_calculator() solution in Solution_Day04.py in OOP concepts 

# implemented solution in imperative form below
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
"""
class my_oops_calculator():
    """
    --------------------
    Exercise 
    -------------------
    Lets implement my_calculator() solution in OOP concepts
    """
    
    def __init__(self,rcv_first_num,rcv_second_num = 1):
            self.first_num = rcv_first_num
            self.second_num = rcv_second_num

    def my_addition(self):
        """receives two numbers from the invoking application and returns addition """
        return self.first_num+ self.second_num

    def my_square(self):
        """ receives two numbers from the invoking application and returns first number squared 2"""
        return str(self.first_num**2)

    def my_exponenation(self):
        """receives two numbers from the invoking application and returns first number raised to number second number"""
        return self.first_num**self.second_num

    @classmethod
    def my_calculator(cls):
        print("****************** MENU ************************")
        print("1: Addition")
        print("2: Square")
        print("3: Exponentation ")
        choice = int(input ("Please select your choice"))
        
        if choice == 1 :
            my_cal_add_object = my_oops_calculator(int(input("Please enter First number:")),int(input("Please enter Second number:")))
            print("The Addition of the numbers is ",my_cal_add_object.my_addition())

        elif choice == 2 :
            my_cal_sqr_object = my_oops_calculator(int(input("Please enter First number:")))
            print("The Square of the number is ",my_cal_sqr_object.my_square())
        elif choice == 3 :
            my_cal_exp_object = my_oops_calculator(int(input("Please enter First number:")),int(input("Please enter Second number:")))
            print("The exponenation of the numbers is ",my_cal_exp_object.my_exponenation())

    @staticmethod
    def iterative_calculator():
        while(True):
            print("Lets start   !!!! ")
            my_oops_calculator.my_calculator()	
            choice = input("\n Do you want to continue (Y/N)").lower()     
            if choice == 'n':
                break

my_oops_calculator.iterative_calculator()    