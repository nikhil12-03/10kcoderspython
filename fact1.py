def factorial(num):
    result=1
    if num==0:
        return result
    while num!=0:
        result*=num
        num-=1
    return result
a=int(input("enter the number:")) 
print(factorial(a))   