
class Node:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self , traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root , "")
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root , "")
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root , "")
        else:
            print('The type is not correct.')
            return

    # root - left - right
    def preorder_print(self , start , traversal):

        if start:  # root is not None
            traversal += (str(start.val) + '-')
            traversal = self.preorder_print(start.left , traversal)
            traversal = self.preorder_print(start.right , traversal)
        return traversal

    # left - root - right
    def inorder_print(self, start , traversal):
        if start:
            traversal = self.inorder_print(start.left , traversal)
            traversal += (str(start.val) + '-')
            traversal = self.inorder_print(start.right , traversal)
        return traversal
    
    # left - right - root
    def postorder_print(self, start , traversal):
        if start:
            traversal = self.postorder_print(start.left , traversal)
            traversal = self.postorder_print(start.right , traversal)
            traversal += (str(start.val) + '-')
        return traversal


tree = BinaryTree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)


print(tree.print_tree('preorder'))