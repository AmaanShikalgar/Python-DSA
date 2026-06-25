def smallest(arr):
    smallest_elem = arr[0]
    for i in arr:
        if(i<smallest_elem):
            smallest_elem = i
    return (smallest_elem)
print(smallest(arr=[12,35,1,10,34]))