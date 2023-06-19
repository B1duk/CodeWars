def sum_two_smallest_numbers(numbers):
    
    list1=[]
    
    min1=min(numbers)
    list1.append(min1)
    
    for num in numbers:
        if num==min1:
            numbers.remove(num)
        else:
            continue
                
    min2=min(numbers)
    list1.append(min2)
    
    count=0
    
    for i in list1:
        count+=i
        
    return count