#task-1
#take a list wchich contains of numbers and add the even numbers to a new list
def evenlist(arr):
    newlist=[]
    for element in arr:
        if element%2==0:
         newlist += [element]
    return newlist
arr=[1,2,3,4,5,6,7,8,9]
print(evenlist(arr))
 
#task-2
#sum of even and odd numbers in list
def sumoflist(li):
   even_sum=0
   odd_sum=0
   for num in li:
      if num%2==0:
         even_sum+=num
      else:
         odd_sum+=num
   return even_sum,odd_sum   
li=[1,2,3,4,5,6,7,8,9] 
print(sumoflist(li)) 


#task-3
#make a word by taking first letter of each element in the list
def first_letter_word(st):
    word=""
    for char in st:
       word+=char[0]
    return ("the word by combining the first letter from every element",word) 
st=["nike","india","kitty","humor","indra","logan"]  
print(first_letter_word(st))
  

#task-4
#reverse a string whithout taking reverse loop
#using slicing
string=str(input("enter the string to be reversed:"))
reversed_string=string[::-1]
print(reversed_string)

#using for loop
def reverse_string(name):
    reverse = ""  # Correct variable name
    for char in name:
        reverse = char + reverse  # Prepend each character
    return reverse

name = "nikhil"
print(reverse_string(name))