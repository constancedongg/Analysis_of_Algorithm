class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_valid_bst(root):
    
    return helper(root)

def helper(root, lowest = float('-inf') , top = float('inf')):
    if not root:
        return True
    
    if root.val <= lowest or root.val >= top:
        return False
    
    return helper(root.left, lowest, root.val) and \
           helper(root.right, root.val, top)

root = Node(2)
root.left = Node(1)
root.right = Node(3)
print(is_valid_bst(root))

root1 = Node(5)
root1.left = Node(1)
root1.right = Node(4)
root1.right.left = Node(3)
root1.right.right = Node(6)
print(is_valid_bst(root1))
'''
    root 2
left 1   right 3
'''

'''

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]

'''