
def reversevowel(s):
    vowels= "aeiouAEIOU"
    result=""
    for char in s:
        if char in vowels:
            result=char+result
    print(result[::-1])        
text=str(input("enter tje text:"))
reversevowel(text)

