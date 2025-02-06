a=4
b=5
add=a+b
sub=a-b
mul=a*b
div=a/b

print(add)
print(sub)
a=8
b=6
print(a*b)
print(a/b)
print(type(div))

#lower bound is included and upper bound is not inclusive in slicing.
#positive indexing --> 0 to (len(str)-1)
#negative indexing-->(-len(str)) to -1

#id() gives the location of value assigned to the variable
#if we assign same value to two different variables, the both variables refer to same id(). and if we modify the value by using one variable then the value change is reflected in the id(), so now when we access the value using another variable the value displayed is modified value but not the initially assigned value.
#if we reassign the value to a new one, the new value assigned will be reflected to both variables and the new value is stored in a new location but the old value's location is not replaced the new one.

#DATA TYPE  -->  structure of data
#String --> Sequence of characters enclosed in "string" or 'string' or '''string'''.
#numerics --> int,float,complex numbers, boolean
#             complex numbers format in python is a+bj. not!!!!  a+bi


#Assignment --> arithmetic operations on complex numbers
#topics discussed --> slicing,negative indexing,string immutable,id(),data types





# str="Problem: Write a function that rotates an array to the right by a given number of steps."
# print(len(str))
# res=str[-88:1]
# print(res)

a=5
b=5
print(id(a))
print(id(b))
a=10
print(id(a))
print(id(b))
print(b)




a=2+3j
b=4+5j
print(a+b)  #6+8j
print(a-b)  #-2-2j
print(a*b)  #8+22j-15=22j-7
print(a/b)  
# print(a//b) #unsupported operand
print(a**b)
print(a%b)  #unsupported operand