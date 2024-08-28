def binary_search(arr, left, right, key):
    if(left > right):
        return False;
    
    pivot = (left + right) // 2

    if(arr[pivot] == key):
        return True

    if(arr[pivot] > key):
        return binary_search(arr, left, pivot-1, key)
    else:
        return binary_search(arr, pivot+1, right, key)
   
if(__name__ == "__main__") :
    print(binary_search([1,2,3,4,5], 0, 10, 3));

# def add(a, b):
#     return a+b
