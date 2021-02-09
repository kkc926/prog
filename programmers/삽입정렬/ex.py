def insertion_sort(arr):
    for i in range(1, len(arr):
        temp = arr[i]
        prev = i - 1
        
        while prev >= 0 and arr[prev] > temp:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = temp