class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def showlist(self):
        while self.head is not None:
            print(self.head.data)
            self.head=self.head.next

list=LinkedList()
list.head=Node("Jan")
e1=Node("Feb")
e2=Node("Mar")
e3=Node("Apr")
#linking first node to second  node
list.head.next=e1
e1.next=e2
e2.next=e3
list.showlist()