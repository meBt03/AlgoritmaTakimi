def bubble_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
        if not swapped:
            break  
    return arr

