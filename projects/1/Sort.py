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
        minloc = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[minloc]:
                minloc = j
            j+= 1
        temp_var = arr[i] 
        arr[i] = arr[minloc]
        arr[minloc] = temp_var
