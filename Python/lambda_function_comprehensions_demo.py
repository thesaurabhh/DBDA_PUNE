# # regular function
# def my_addition(first_num,second_num):
#     """receives two numbers from the invoking application and returns addition """
#     return first_num+ second_num

# # invoking regular function
# print(my_addition(1,2))

# # lambda function
# # lambda inputparam : return_expression
# my_lamdba_add_func = lambda first_num,second_num :  first_num+ second_num

# # invoking lambda function
# print(my_lamdba_add_func(1,2))

# # definitions 
# def my_square(first_num):
#     """receives two numbers from the invoking application and returns first number squared 2 """
#     return str(first_num**2)

# my_lambda_square_func = lambda first_num : str(first_num**2)

# # invocation
# # print(my_square(5))
# # print(my_lambda_square_func(5))

# # Higher order function
# def my_higher_order_func (l_func,*args):
#     print(f"I am higher order function with arguments {l_func, *args}")
#     print(l_func(*args))
    
# # invocation of HOF    
# my_higher_order_func(my_lambda_square_func,5)
# my_higher_order_func(my_lamdba_add_func,1,2)


# """
# -----------------------------------------------------------------------
# EXERCISE on lambda and Higher Order Functions
# -----------------------------------------------------------------------
# 1) ******** Convert following functions from function_definitions.py into lambda *****    
# 2) ******** Create HOF so that each of the above created lambda functions can be invoked 
#             using a single HOF *****                
# """            

#****************** Solutions provided in Solutions_Day10.py ****************


# list comprehension
my_list_comprehension = list(elem for elem in "gaurav" )
my_list_comprehension1 = [elem for elem in "gaurav" ]   

# tuple comprehension
my_tuple_comprehension = tuple(elem for elem in "gaurav" )
  
# set comprehension
my_set_comprehension = set(elem for elem in "gaurav" )  
 
# dict comprehension
my_dict_comprehension = dict( ("key"+elem, "value"+elem)  for elem in "gaurav" )  
my_dict_comprehension1 = { "key"+elem : "value"+elem  for elem in "gaurav" }

# generator comprehension
my_generator_comprehension = (elem for elem in "gaurav" )

print("my_list_comprehension is " , my_list_comprehension)
print("my_list_comprehension1 is " , my_list_comprehension1)
print("my_tuple_comprehension is " , my_tuple_comprehension)
print("my_set_comprehension is " , my_set_comprehension)
print("my_dict_comprehension is " , my_dict_comprehension)
print("my_dict_comprehension1 is " , my_dict_comprehension1)
print("my_generator_comprehension is " , my_generator_comprehension)
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")
print(next(my_generator_comprehension),end = " ")

# before walrus operator 
val = int(input ("Please enter a numeric value "))
if (val == 10 ):
    print("HI") 

# after walrus operator
if (val := int(input ("Please enter a numeric value ")) == 10 ):
    print("HI") 