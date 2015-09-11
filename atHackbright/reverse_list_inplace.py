def reverse_list(my_list):
    length = len(my_list)-1
    temp=0
    print "Reverse this list:",my_list
    for i in range(len(my_list)/2):
        first = my_list[i]
        last = my_list[length]
        temp = first
        my_list[i] = last
        my_list[length] = temp
        length -=1
        print my_list
    
    return my_list
        
    
    
reverse_list([1,2,4,5,6,7]) 
reverse_list([3,4,7,9,10,])   