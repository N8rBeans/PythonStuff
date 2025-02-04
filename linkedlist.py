class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp)
            temp = temp.next

        print("List Complete")

    def append(self, value):
        new_node = Node(value)

        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)

        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def deleteHead(self):
        if(self.length == 0):
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1
        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp

    def deleteTail(self):
        if(self.length == 0):
            return None

        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None

        self.length -= 1
        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp


myLinkedList = LinkedList(5)

# expected: 5

myLinkedList.append(6)
myLinkedList.prepend(7)
myLinkedList.prepend(8)
myLinkedList.append(9)

# expected: 8, 7, 5, 6, 9

myLinkedList.deleteHead()

# expected: 7, 5, 6, 9

myLinkedList.deleteTail()

# expected: 7, 5, 6

myLinkedList.print_list()
