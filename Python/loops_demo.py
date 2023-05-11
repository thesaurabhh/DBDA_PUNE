"""
# basic syntax for conditionals and loops in python
if condition:
    if block	
	
if condition:
    if block	
else:
    else block

if condition1:
    if block1
if condition2:
    if block2	
else:
    else block

for i in sequence_type:
   body of for 

while(condition):
	body of while

"""
num=1 
while(num<10):
     print(num, end = " ")
     num+=1
     break

num=1 
while(num<10):
     print(num, end = " ")
     num+=1
     continue
 
 
num=1 
while(num<10):
     print(num, end = " ")
     continue
     num+=1

# if i want to print 1-5 but loop for 1-9
num=1 
while(num<10):
     if num<6 : 
        print(num, end = " ")
     num+=1

       

# prints 2-10
num=1 
while(num<10):
     if num<6 : 
        pass
     num+=1
     print(num, end = " ")

# range(start, stop,step_size)
print(list(range(2,20,3)))
print(list(range(2,20)))
print(list(range(4))) #print(list(range(0,4)))

# ***********************************************************
# Practice problem 1 
# ***********************************************************
# Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game

# TEST CASES:

# 50 : BUZZ    
# 30 : FIZZ BUZZ
# 9 : FIZZ
# 22 : Invalid input

#********* Solution provided in Solutions_Day04.py