def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    
    n=len(unsorted_list)
    for i in range(n-1):
     for j in range (n-i-1):
        if unsorted_list[j]>unsorted_list[j+1]:
           unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]
    
    return unsorted_list


print(bubble_sort([3,2,1]))