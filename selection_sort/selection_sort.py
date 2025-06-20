def selection_sort(arr):

    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    
    return arr

print(selection_sort([1, 2, 3]))  # Should return [1, 2, 3]
print(selection_sort([3, 2, 1]))  # Should return [1, 2, 3]
print(selection_sort([29, 10, 14, 37, 14]))  # Should return [10, 14, 14, 29, 37]
