# # variable scope demonstration 
# from function_definitions import *

# def my_iterative_calculator():
#     exponentation_num = 2
#     pi = 3.1416
#     some_list = [1,2,3,4]
    
#     def my_inner_calculator_func():
#         input_num = 2 
#         #global pi #nonlocal pi
#         pi = 3.14
#         some_list = [5,6,7,8]
#         #some_list[1] = 100
        
#         def one_more_inner_calculator_func():
#             #nonlocal pi
#             pi = 40000000
#             some_list = [9,10,11,12]
#             #some_list[2] = 100000
#             print("Inside one_more_inner_calculator_func pi:       ",pi)
#             print("Inside one_more_inner_calculator_func somelist[]   :       ",some_list)
            
#         one_more_inner_calculator_func()
#         print("Inside my_inner_calculator_func pi:       ",pi)
#         print("Inside my_inner_calculator_func somelist[]   :       ",some_list)

#     my_inner_calculator_func()   
#     print("Inside my_iterative_calculator pi:       ",pi)
#     print("Inside my_iterative_calculator somelist[]   :       ",some_list)


# my_iterative_calculator()
# print("module level pi:       ",pi)



# ###### globals() and locals() demonstration below #######
# # globals at any point gives you global definitions
# import function_definitions
# print("1:       ",globals())

# from function_definitions import *
# print("2:       ",globals())

# def my_iterative_calculator():
#     exponentation_num = 2
#     pi = 3.1416
    
#     def my_inner_calculator_func():
#         input_num = 2 
#         pi = 3.14
        
#         def one_more_inner_calculator_func():
#             nonlocal pi
#             pi = 40000000
#             print("3:       ",globals())
            
#         one_more_inner_calculator_func()
#         print("4:       ",globals())
          
#     my_inner_calculator_func()   
#     print("5:       ",globals())

# my_iterative_calculator()

# locals at any point gives you local definitions
import function_definitions
print("1:       ",locals())

from function_definitions import *

print("2:       ",locals())

def my_iterative_calculator():
    exponentation_num = 2
    pi = 3.1416

    def my_inner_calculator_func():
        input_num = 2 
        pi = 3.14
        
        def one_more_inner_calculator_func():
            nonlocal pi
            pi = 40000000
            print("3:       ",locals())
            
        one_more_inner_calculator_func()
        print("4:       ",locals())
          
    my_inner_calculator_func()   
    print("5:       ",locals())

my_iterative_calculator()
