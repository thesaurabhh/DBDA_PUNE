# 1) Inheritance 
class Parent:
    
    # class variable
    parent_class_variable = "parent_class_variable"
    
    # class method (decorator/ annotation used below to mark the method as class method)
    @classmethod
    def get_parent_class_variable(cls):
        return cls.parent_class_variable
    
    # class method (decorator/ annotation used below to mark the method as class method)
    @classmethod
    def set_parent_class_variable(cls, new_value):
        cls.parent_class_variable = new_value

    # constructor/ Initialiser
    def __init__(self, rcv_val1,rcv_val2):
        self.parent_instance_variable1 = rcv_val1
        self.parent_instance_variable2 = rcv_val2
    
    # instance method
    def get_parent_instance_variable1(self):    
        return self.parent_instance_variable1;

    # instance method
    def set_parent_instance_variable1(self,new_value):    
        self.parent_instance_variable1 = new_value
    
    # instance method
    def display_parent_object(self):
        print(self.parent_instance_variable1 + '    ' + self.parent_instance_variable2)
        
# child class inheriting from Parent class 
class Child(Parent):
    pass

# object creations and invocations    
# creating the child_object
child_object = Child("initiailised_value1","initiailised_value2")

# displaying the child object instance variables 
child_object.display_parent_object()

# setting an instance variable
child_object.set_parent_instance_variable1("updated_value1")

# displaying the child object instance variables 
child_object.display_parent_object()


# 2) regular expressions

# this package helps you write regular expression in python
import re 
pattern = '[a-z]+'
string_to_apply = "test_string"

# searches the string_to_apply with the pattern provided 
result= re.search(pattern,string_to_apply) 

print(result.group(0)) # returns the matched result 

# for understanding how differnt regular expression are written refer Basic concepts of wiki
# https://en.wikipedia.org/wiki/Regular_expression

# 3) Exception Handling 

my_list = [100]

# this below code should raise an IndexError exception since index 1 is not present in my_list
if my_list[1] == 100:
    print("I accessed the first element of my list ")
    

# exception handled code     
try:
    if my_list[1] == 100:
        print("I accessed the first element of my list ")
except Exception:
    print("Exception is now handled using Exception exception  ")        
finally:
    print("Finally block is executed no matter what -- with or without exception")    
    

# specific exception handled code     
try:
    if my_list[1] == 100:
        print("I accessed the first element of my list ")
except IndexError:
    print("Exception is now handled using IndexError exception ")        
except Exception:
    print("Exception is now handled using Exception exception  ")        
finally:
    print("Finally block is executed no matter what -- with or without exception")    



# 4) File Handling 
try:
    # try to read a file that does not exists by opening it in read operation mode
    file1 = open('unexisting_file.txt',"r")
except FileNotFoundError:
    print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
    # try to write to a file that does not exists by opening it in write+ operation mode
    # should create a file for you and write something to it 
    file1 = open('unexisting_file.txt',"w+")
    file1.write("Default creation was done in exception block")
    file1.close()

file1 = open('unexisting_file.txt',"r")
print(file1)
print(file1.read())
# 5) Lambda Functions 
# also called as anonymous functions

# lambda inputparam : return_expression
add_2_num_lambda = lambda num1,num2 : num1+num2

# return_val_from_lambda_func = add_2_num_lambda(1,2)
# print(return_val_from_lambda_func)

# 6) Higher order function
def my_hof(rcv_func_reference,val1,val2):
    return rcv_func_reference(val1,val2)

# calling HOF
print(my_hof(add_2_num_lambda,1,2))


# 7) list comprehension

my_list = [ elem for elem in "1234567890"]
print(my_list)