class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1    

    def pop(self):
        if (self.head is None) and (self.tail is None):
            print("nai")
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            self.tail = temp
            temp.next = None
            self.length -= 1

    def prepend(self,value):
        node = Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
        self.length+=1

    def popFirst(self):
        if (self.head == None) and (self.tail==None):
            print("nai nai")
        elif self.head.next is None:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.length-=1        
        
    def get(self,index):
        if (self.length<=index) or (index<0):
            print("invalid index")
        else:
            count = 0
            temp = self.head
            while(count!=index):
                temp = temp.next
                count+=1
            print(temp.value)    

    def set_value(self, index, value):
        if (self.length<=index) or (index<0):
            print("invalid")
        else:
            count=0
            temp=self.head
            while(count!=index):
                temp=temp.next    
                count+=1
            temp.value=value

    def insert(self,index,value):
        if (self.length<index) or (index<0):
            print("invalid")
        elif (index==0):
            self.prepend(value)
        elif (index==self.length):
            self.append(value)
        else:
            node=Node(value)
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            node.next=temp.next
            temp.next=node
            self.length+=1

    def remove(self,index):
        if (self.length<index) or (index<0):
            print("invalid")
        elif (index==0):
            self.popFirst()
        elif (index==self.length):
            self.pop()
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
            self.length-=1    
        
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
my_linked_list = LinkedList(4)
my_linked_list.print_list()

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.print_list()

my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
my_linked_list.print_list()

my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()

print("Initial List: ")
my_linked_list.prepend(4)
my_linked_list.prepend(3)
my_linked_list.print_list()

print("New List: ")
my_linked_list.popFirst()
my_linked_list.popFirst()
# # my_linked_list.popFirst()
my_linked_list.print_list()

# my_linked_list.get(-1)
# my_linked_list.get(8)
# my_linked_list.get(2)

# my_linked_list.set_value(2,9)
# my_linked_list.print_list()

# my_linked_list.insert(4,10)
# my_linked_list.print_list()

# my_linked_list.remove(4)
print("Reversed-List: ")
my_linked_list.reverse()

my_linked_list.print_list()

