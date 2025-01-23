def fun(num):
    sum=0
    while num!=0:
        dig=num%10
        sum=sum+dig
        num=num//10
    return sum    
a=int(input("enter the number:"))
output=fun(a)
print(output)
