def second_max_num(l):
    max_val=float('-inf')
    sec_max=float('-inf')
    for num in l:
        if num > max_val:
            sec_max=max_val
            max_val=num
        elif num > sec_max and num!=max_val:
            sec_max=num
    return sec_max if sec_max !=float('-inf') else None

numbers=[1,2,3,4,5,6,7,7,8,9,9]
print('second maximum number from list is:',second_max_num(numbers))
