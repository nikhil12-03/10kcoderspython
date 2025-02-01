#Jump Statements- break,continue,pass

#Break and Continue -used in loops
# the below program will print the even numbers 
# from 0 to 20 and using while lop . it breakes the loop when 
#i value reaches 9
i=0
while i<=20:
   
    if i%2==0:
        print(i)
    if i==0:
        break
    i+=1    


#Continue-skipps that particular iteration
#once the continue is hit by the compiler the statements after
# continue in that loop will stop executing and continue the loop based on the condition
for i in range(0,21):
    print(i,'iteration')
    if i==8 or i==0:
        continue
    print(i) 

#continue and break in nested for loop
#the break statement will only brekas the loop in which it is writen
#and doesnot disturb the outer loops
for cls1 in range(1,10):
    for roll in range(1,20):
        if cls1==5:
            break
        print(cls1,roll)  


#pass statement
#to avoid leaving the block empty we use pass statement
num=15
if num % 4==0:
    #instead of leaving the block empty when wedont want to include code in if-block we use pass
    pass
else:
    print('pass statement is used')

#we can use pass where ever we have to say that the block is empty
# pass in function
def example():
    pass   
#in this example we passed a function with pass satement 
#instead of leaving it empty which will raise error 