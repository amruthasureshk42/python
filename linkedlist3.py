class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval =printval.next
list1=SLinkedList()
list1.head=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list1.head.next=e2
e2.next =e3
list1.listprint()
