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


for cls1 in range(1,10):
    for roll in range(1,20):
        if cls1==5:
            break
        print(cls1,roll)  
          