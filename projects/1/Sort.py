def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k 
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j-=1 
        arr[j] = cur

def selection_sort(arr): 
    for i in range(0,len(arr)):
        pass

    while True:
        if True:
            pass
