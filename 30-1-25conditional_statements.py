# # # # the statements which controlls the flow of execution of the code
# # # # conditional statements ,loops,jump statements
 
# # # #example for check number is even or odd
# num=int(input("enter the number to check its even or odd:"))
# if num%2==0:
#     print(f"the number{num} is even ")
# else:
#     print(f"the number {num} is odd")    


# # # #nested if-else
# num1=int(input("enter number"))
# if num1>0:
#     print("the number is positive")
# if num1 ==1:
#        print("One")
# else: 
#     if num == 0:
#         print("Zero")  
#     else:
#       print("the number is negative")

# # # #else-if -> elif:
      

# current_units=int(input("enter the no of units:"))
# if current_units <=100 :
#     if current_units<=50:
#            print("the current bill is:",current_units*0)
#     else:   
#            print("current bill =",current_units*50) 

# else:
#   if 300>current_units>200:
#         print("current bil=",current_units*150)
#   else:
#        print("current bill=",current_units*100)


# # # #Loops
# # # #for,while

# for i in range(0,21,2):
#     print(i)

# for num in range(1,101,2):
#     print(num,'odd')

# # #nested for loop
# for i in range(0,11):
#     for num in range(0,5):
#         print(i)


# for a in range(1,11):
#     if a!=5 and a!=7:
#         for b in range(1,31):
#             print(a,b)        


#  #while loop
# num1=8
# while num1 <=8:
#      print('hii')
# num1=0
# while num1<26:
#     if num1 % 2==0:
#         print(num1,'even')
#     else:
#         print(num1,'odd')    
#     num1=num1+1    
# j=1
# while j < 11:
#     i=0    
#     if j!=5 and j!=7:
#         while i < 31:
#             print(j,i)
#         i+=1
#     j+=1        


#terinary opertor
num1 = '10' if num2 %10==0 else num1 = 8