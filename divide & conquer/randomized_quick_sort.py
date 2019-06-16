
'''
Randomized version of quick sort, when we use random sampling to choose pivot.

Why we need randomized quick sort?
- To get the average case of running time, when randomness is gained over input.

'''
import random 
def random_quick_sort(arr , left , right):
    if left < right:
        split = Partition(arr , left , right)
        random_quick_sort(arr , left , split - 1)
        random_quick_sort(arr, split + 1 , right)


def Partition(arr , left , right):
    
    # randomness of pivot
    rand = random.randint(left, right)
    arr[rand] , arr[right] = arr[right] , arr[rand]
    pivot = arr[right]

    split = left - 1
    for i in range(left , right):
        if arr[i] <= pivot:
            arr[i] , arr[split + 1] = arr[split + 1] , arr[i]
            split += 1

    arr[right] , arr[split + 1] = arr[split + 1] , arr[right]
    split += 1

    print(pivot , arr)

    return split

arr = [1,3,7,2,6,4,5]
random_quick_sort(arr , 0 , len(arr) - 1)
