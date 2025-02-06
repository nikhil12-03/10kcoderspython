#1 print 1-100 using while
#2 print same as 1 but reverse using for and while
#3 reverse a number using while without string conversion


#3
def reverse(num):
    l= 0
    r=0
    for i in num:
        last=int(num%10)
        r +=l
        mun=num//10
    return r
a=input("enter the number:")
print(reverse(a))    

