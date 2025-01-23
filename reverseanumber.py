def reversenum(num):
    result=0
    last=0
    while(num!=0):
        last=num%10
        result=(result*10)+last
        num=num//10
    return result
numb=int(input("enter the number:")) 
print(reversenum(numb))


