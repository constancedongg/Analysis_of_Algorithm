class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# class Tree:
#     def __initi__(self, root):
#         self.root = Node(root)

#     def print_tree(self, root):
#         print(self.root.value)

def print_pre(root):

    if root:
        print(root.value)

        print_pre(root.left)
        print_pre(root.right)
   
def print_post(root):
    if root:
        print_post(root.left)
        print_post(root.right)
        print(root.value)

def print_in(root):
    if root:
        print_in(root.left)
        print(root.value)
        print_in(root.right)

       
# if __name__ == '__main__':
# root = Node(3)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

root = Node(1)
# root.left = Node(9)
root.right = Node(2)
root.right.left = Node(3)
# root.right.right = Node(7)

print('\nPreorder:\n')
print_pre(root) # [3,9,20,15,7]

# print('\nPost-order:\n')
# print_post(root) # [9,15,7,20,3]

# print('\nIn-order:\n')
# print_in(root) # [9,3,15,20,7]


