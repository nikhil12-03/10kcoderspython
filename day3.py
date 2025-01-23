# arithematic operations on complex numbers
n=3+7j
b=4-3j
print(n+b)
print(n-b)
print(n/b)
print(n**b)
print(n*b)
print(n%b)#---notsupported and throws type error
print(n//b)#--notsupported and throws type error


# #Boolean - TRUE/FALSE
"""checks the values on bothsides are equal or not
   and gives output as true or false 
"""
a=123
print(a==456) #----False
print(a==123) #----True
# thi sis an example which takes password from user and checks the password from database 
db_user_password="12345678"
user_password_input=str(input("enter password:"))
if db_user_password == user_password_input:
    print("login succesful")
else :
    print("incorrect password")    

print(int(False)) #-- this gives the integer value of False (which is'0')



# # sequences- strings, tuples, list, range
  
#   #LIST - is a collection of data elements which are of different data types
list_new=[1,2,3,4,5,[6,7,"hello",9],"name"]
print(list_new[5])
print(len(list_new))
print(list_new[-1])
print(list_new[1:7:2]) 
print(list_new[::-1])
print(list_new[5][2]) #--- accessing list inside a list (listnew[index][inside list index])
list_new[3]=5
list_new[5][2]="goodnight"
print(list_new)
print(len(list_new[5]))
print(list_new[-1::-2])
print(list_new[0::2])
print(list_new[1::2])
print(len(list_new[5][2])) 

 #Tuples  --it is sam eas list but its is immutable
tup=(1,2,3,4)
tup1=5,6,7,8 #both tup and tup1 are tuples .these are more memory efficient.faster than list.
#The tuple is mostly depends on the coma which seperates the elements in it and not on the parenthesis which encloses them
print("tup",type(tup))
print("tup1",type(tup1))
print(tup[::-1]) #we can access the tuple elements same as list
print(tup[2:])
print(tup[-1::-2])


#range
print(list(range(0,100,2)))#prints even numbers within range
print(list(range(1,100,2)))#prints odd numbers within range
print(list(range(100,0,-1)))

