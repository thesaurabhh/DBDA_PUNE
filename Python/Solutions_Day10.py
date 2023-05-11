"""
-----------------------------------------------------------------------
EXERCISE on lambda and Higher Order Functions
-----------------------------------------------------------------------
1) ******** Convert following functions from function_definitions.py into lambda *****    
2) ******** Create HOF so that each of the above created lambda functions can be invoked 
            using a single HOF *****                
""" 


"""def my_addition(first_num,second_num):
    #receives two numbers from the invoking application and returns addition 
    return first_num+ second_num"""

my_addition=lambda num1,num2:num1+num2
print(my_addition(1,2))

"""def my_square(first_num):
    #  receives two numbers from the invoking application and returns first number squared 2 
    return str(first_num**2)"""

my_square=lambda num1:num1**2
print(my_square(2))

"""def my_exponenation(first_num,second_num):
# receives two numbers from the invoking application and returns first number raised to number second number
    return first_num**second_num"""

my_exponenation=lambda num1,num2:num1**num2
print(my_exponenation(2,3))


"""def my_uppercase_func(received_string):
    # 2) receives String and returns upper case of the input string
    return received_string.upper()
"""
my_uppercase_func=lambda string:string.upper()
print(my_uppercase_func("test"))

"""
def raise_sal_percent(existing_salary,raise_salary_percentage):
    #receives "raise_salary_percentage" , salary raise ,
    #percentage from the user, 
    #returns the incremented salary to the console
    return existing_salary + (existing_salary*raise_salary_percentage/100) 
"""
raise_sal_percent=lambda existing_salary,raise_salary_percentage:existing_salary + (existing_salary*raise_salary_percentage/100)
print(raise_sal_percent(900,10))


"""def get_height(height):
   # receives height from the user in cms and returns the user height back in foot/feet and inches
    return round((height/30.48),2)"""

get_height=lambda height:round((height/30.48),2)
print(get_height)

"""def convert_to_rupee(no_of_dollars):
   # receive no of the dollars from the user apply the conversion of 
   # 1 dollar = 82 rupees and return the amount to the console in rupees
    return no_of_dollars*82"""

convert_to_rupee=lambda no_of_dollars:no_of_dollars*82
print(convert_to_rupee(50))

"""def get_fare_details(source, destination, fare_in_INR, discount_rate_percentage):
    6) receive source, destination, fare in INR, discount_rate percentage from the user and return the 
    string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
    return "Fare from" + source +" to " + destination + " is " + str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100) ) + " INR with has a applied discount of " + str(discount_rate_percentage)+ "%"
"""
get_fare_details= lambda source, destination, fare_in_INR, discount_rate_percentage:"Fare from" + source +" to " + destination + " is " + str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100) ) + " INR with has a applied discount of " + str(discount_rate_percentage)+ "%"
print(get_fare_details('Mumbai', 'Pune', 300, 10))

    
"""def my_addition_arbitary_positional(*numbers)
    1) receives two numbers from the invoking application and returns 
        a) addition 
    sum = 0 
    for num in numbers:
        sum = sum+ num
    return sum"""


# lambda function (Note the use of walrus operator)
my_addition_arbitary_positional= lambda sumq,*numbers : [ sumq:=sumq+i for i in numbers ]
o_sum = 0 
print(my_addition_arbitary_positional(o_sum,1,2,3))


# without lambda using only list comprehensions         
o_sum = 10 
def my_addition_arbitary_positional(sumq,*numbers) :
    return [sumq :=sumq+i  for i in numbers]
                  
print(my_addition_arbitary_positional(o_sum,1,2))     

# using lamdba inside another lambda
temp_sum = lambda val1,val2 : val1 + val2
my_addition_arbitary_positional= lambda sumq,*numbers : [ sumq := temp_sum(sumq, i) for i in numbers ]
o_sum = 0 
print(my_addition_arbitary_positional(o_sum,1,2,3))

# normal list operation
o_sum = 0 
def my_addition_arbitary_positional(sumq,*numbers) :
    return_list = [] 
    for i in numbers :
         sumq = sumq+i
         return_list.append(sumq )
    return return_list   
print(my_addition_arbitary_positional(o_sum,1,2,3))


"""
def my_addition_arbitary_keyword(**numbers_dict):
# receives two numbers from the invoking application and returns addition 
    sum = 0 
    for num in numbers_dict.values():
        sum = sum+ num
    return sum 
"""

# lambda function (Note the use of walrus operator)
l_my_addition_arbitary_keyword= lambda sumq,**numbers_dict : [ sumq:=sumq+i for i in numbers_dict.values() ]
o_sum = 0 
print(l_my_addition_arbitary_keyword(o_sum,val1= 1, val2 = 2,val3 = 3))


