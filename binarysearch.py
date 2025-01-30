def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
           return mid
        elif arr[mid]<target:
            left =  mid
        elif arr[mid]>target :
            right=mid     
    return -1 
arr=[0,1,2,3,4,5,6,7,8,9]
target=int(input("enter the target to be found:"))
result=binary_search(arr,target)  
if result==-1:
    print("the item is not found")
else:    
   print(f"the target is found at :{result}")