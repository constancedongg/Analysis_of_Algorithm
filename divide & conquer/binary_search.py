

'''
Binary search: search a sorted array, return the index of the searching input or -1 if not find.
Correctness can be proved by induction.
T(n) = T(n / 2) + O(1) , a = 1, b = 2, k = 0, since a = b^k = 1 , O(n^k * logn)
Time Complexity: O(logn)
'''

def binary_search(A , x , left , right):
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
        return binary_search(A , x , left , right)

A = [0 , 2 , 3 , 6 , 10]
x = 2
left = 0
right = len(A) - 1
print(binary_search(A , x , left , right))
