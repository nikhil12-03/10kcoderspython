def getmiddle(s):
    length=len(s)
    middle=length//2
    print("length of string:",length)
    print(middle)
    if (length%2==0):
       return s[middle-1:middle+1]
    else:
        return s[middle]
a=str(input("enter the string:"))       
print(getmiddle(a))