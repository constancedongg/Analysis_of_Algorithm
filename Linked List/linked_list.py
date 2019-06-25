
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Linkedlist:
    # input is ListNode object initialized with value root
    def __init__(self , root):
        self.root = ListNode(root)

    def return_list(self, start , linkedlist):

        if start:
            linkedlist += (str(start.val) + '->')
            linkedlist = self.return_list(start.next , linkedlist)
        return linkedlist

    def print_list(self):
        return self.return_list(self.root , "")
        

l1 = Linkedlist(3) 
l1.root.next = ListNode(0)
l1.root.next.next = ListNode(2)
print(l1.print_list())



def print_ll(root):
    if root:
        print(root.val)
        print_ll(root.next)


root1 = ListNode(10)
root1.next = ListNode(2)
print_ll(root1)