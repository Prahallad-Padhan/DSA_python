class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegining(data)
            return
        pos = 0
        temp = self.head
        while temp.next is not None and pos+1 != index:
            pos +=1 
            temp = temp.next
        if temp is not None:
            newNode = Node(data)
            newNode.next = temp.next
            temp.next = newNode
        else:
            print("index not present")

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBegining(2)
    ll.insertAtEnd(3)
    ll.insertAtEnd(5)
    ll.insertAtBegining(1)
    ll.insertAtIndex(4,3)
    ll.printList()