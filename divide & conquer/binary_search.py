

'''
Binary search: search a sorted array, return the index of the searching input or -1 if not find.
Correctness can be proved by induction.
T(n) = T(n / 2) + O(1) , a = 1, b = 2, k = 0, since a = b^k = 1 , O(n^k * logn)
Time Complexity: O(logn)
'''

#=============== interactive ==============#

def binary_search(A , x):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1

arr = [0,2,5,6,9]
target = 9
print(binary_search(arr , target))


#=============== recursive ===============#
def binary_search1(A , x , left , right):
    mid = left + (right - left) // 2
    if x == A[mid]:   
        return mid
    elif left > right:
        return -1
    else:
        if x > A[mid]:
            left = mid + 1

        else:
            right = mid - 1

        # when using recursive algorithm, do not forget the return here, otherwise, return nothing
        return binary_search1(A , x , left , right)

A = [0 , 2 , 3 , 6 , 10]
x = 2
left = 0
right = len(A) - 1
print(binary_search1(A , x , left , right))


def binary_search2(num , target , start , end):


    if start < end:
        mid = (start + end) // 2

        if num[mid] == target:
            return mid

        elif num[mid] < target:
            return binary_search2(num, target , mid + 1 , end)
        
        else:
            return binary_search2(num , target , start , mid)
    else:
        return -1


print(binary_search1(arr , target , 0 , len(arr)))