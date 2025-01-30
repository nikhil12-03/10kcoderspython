def second_min_num(l):
    min_val=float('inf')
    sec_min=float('inf')
    for num in l:
        if num < min_val:
            sec_min=min_val
            min_val=num
        elif num > min_val and sec_min > num:
            sec_min=num
        else:    
          return sec_min if sec_min !=float('inf') else None

numbers=[1,2,3,4,5,6,7,7,8,9,9]
print('second minimum number from list is:',second_min_num(numbers))
