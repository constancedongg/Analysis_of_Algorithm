
'''
Quicksort is a divide and conquer algorithm （recursively break down the problem into sub problems);
in-place algorithm; 
worst-case running time is Θ(n2) ; its average-case running time is Θ(n log n)

Main idea:  Pick an input item, call it pivot, and place it in its final location in the sorted array by re-organizing the array (just pick the last item of arr as pivot)
            so that:
             all items ≤ pivot are placed before pivot
             all items > pivot are placed after pivot

'''

# in-place algorithm, nothing to return
def quick_sort(arr , left , right):
    if left < right:      
        split = Partition(arr, left, right)
        quick_sort(arr , left , split - 1)
        quick_sort(arr , split + 1 , right)
 



def Partition(arr , left , right):
    pivot = arr[right]
    split  = left - 1
    for i in range(left , right):
        if arr[i] <= pivot:
            arr[i] , arr[split + 1] = arr[split +  1] , arr[i]
            split += 1

    arr[right] , arr[split + 1] = arr[split + 1] , arr[right]
    split += 1
    return split


arr = [1,3,7,2,6,4,5]
quick_sort(arr, 0 , len(arr) - 1)