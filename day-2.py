#Boolean=True or False.(Default=False)
#applications--> Atm pin, username and password
#  
#DATA TYPES
#numeric--!
#Sequences-->Strings,List,Tuple,Range.

#Array-->collections of homogeneous elements
#List in [] -->collection of heterogeneous elements
#list is mutable*****,can accept diff data types,indexing is possible
#ITERATION is slower in list**********
#List is not memory Efficient*****  

#Tuple-->collection of heterogeneous elements
#Tuple is IMMUTABLE****,can accept diff dat atypes,indexing is possible.
#ITERATION is faster in list**********
#Tuple is memory Efficient******

#Range--> (lower bound,upper bound)
#print(range(0,100))--> output is range(0,100)
#even num-->range(0,100,2)
#odd num-->range(1,100,2)



lst=[2,3,4,"str",False,[1,"bye",3]]
print(lst)
print(lst[3])
print(len(lst))
print(lst[5])
print(lst[-2])
print(lst[1:3:2])
# print(lst[6])
print(lst[-1][1])
lst[5][-1]="hello"
print(lst)
print(len(lst[5]))
print(len(lst))
print(len(lst[5][1]))
for i in range(0,len(lst)):
    print(lst[i])


#Datatypes : strings,list,tuple,range,boolean

#List: it is a collection of elememts of different datatypes
my_list = [1,2,3,"str",["hey",-2,-4,0]]
print(type(my_list)) #<class 'list'>
print(my_list[0]) #1
print(my_list[-1]) #[-2,-4,0]
print(my_list[4][2]) #0
print(len(my_list)) #5
print(len(my_list[4][0])) #3

#Tuple: it is a collection of elememts of different datatypes but the main difference between list and tuple is it is immutable.
# list vs tuple:
# --> list is mutable whereas tuple is immutable
# --> list is slower whereas tuple is faster
# --> tuple's memory is more efficient as it is immutable so nothing changes
my_tuple1 = ()
my_tuple2 = (1,2,"heylo",24.5,(67,89,43),[78,"misty"])
print(my_tuple2[0]) #1
print(my_tuple2[4][2]) #43
print(my_tuple2[5][1]) #misty

# range : (lower,upper) --> lower(inclusive) && upper(exclusive)
# range(0,10)
# range(0,10,-1)
# range(0,10,2)
# range(10,0,-1)

#boolean : True or False 
# true --> 1
# false --> 0

# print(123=="123")