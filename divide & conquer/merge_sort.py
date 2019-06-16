

'''
Divide & Conquer algorithm
Master Theorem: T(n) = a * T(n / b) + O(n ^ k)
Here, a = 2, b = 2 , n = 1, a = b^k O(n^k*logn)
Time complexity: O(nlogn)
Space complexity: O(n)
'''

def merge_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list

    middle = len(unsorted_list) // 2

    left_unsort = unsorted_list[ :middle]
    right_unsort = unsorted_list[middle: ]
    left_sorted = merge_sort(left_unsort)
    right_sorted = merge_sort(right_unsort)
    return list(merge(left_sorted , right_sorted))


def merge(left_half , right_half):
    res = []
    while len(left_half) and len(right_half):
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    if len(left_half) != 0:
        res = res + left_half
    elif len(right_half) !=0:
        res = res + right_half
    return res


# unsort = [6 , 2 , -5 , 10 , 8]
unsort = ['a' , 'n' , 'b' , 'a']
print(merge_sort(unsort))