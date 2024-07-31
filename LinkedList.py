class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length=1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1
    
    def pop(self):
        if (self.head == None) and (self.tail==None):
            print("Not available")
        elif self.head.next==None:
            self.head=None
            self.tail=None
            self.length-=1
            print("Not available")
        else:    
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            self.tail=temp
            self.tail.next=None


my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
my_linked_list.pop()


my_linked_list.print()
