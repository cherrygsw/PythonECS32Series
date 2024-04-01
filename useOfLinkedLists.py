class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node

class Stack2:
    def __init__(self):
        self.mainQueue = Queue()
        self.helperQueue = Queue()

    def isEmpty(self):
        return self.mainQueue.isEmpty()

    def push(self, item):
        # Move all elements to helper queue
        while not self.mainQueue.isEmpty():
            self.helperQueue.enqueue(self.mainQueue.dequeue())
        # Enqueue the new item to main queue
        self.mainQueue.enqueue(item)
        # Move everything back
        while not self.helperQueue.isEmpty():
            self.mainQueue.enqueue(self.helperQueue.dequeue())

    def pop(self):
        if not self.isEmpty():
            return self.mainQueue.dequeue()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.mainQueue.items[-1]
        else:
            return None

    def size(self):
        return self.mainQueue.size()

def transform(lst):
    pythonList = []
    currentNode = lst
    while currentNode:
        pythonList.append(currentNode.data)
        currentNode = currentNode.next
    return pythonList

def concatenate(lst1, lst2):
    if lst1 is None:
        return lst2
    if lst2 is None:
        return lst1

    # Find the last node of lst1
    lastNode = lst1
    while lastNode.next:
        lastNode = lastNode.next
    lastNode.next = lst2
    return lst1

def removeNodesFromBeginning(lst, n):
    currentNode = lst
    while n > 0 and currentNode:
        currentNode = currentNode.next
        n = n - 1
    return currentNode

def removeNodes(lst, i, n):
    if i == 0:  # Special case: start at the head
        while n > 0 and lst:
            lst = lst.next
            n -= 1
        return lst

    currentNode = lst
    for _ in range(1, i - 1):  # Move to the (i-1)th node
        if currentNode is None:
            return lst  # i is out of bounds
        currentNode = currentNode.next

    # Remove n nodes after currentNode
    nextNode = currentNode.next
    for _ in range(n):
        if nextNode is None:
            break
        nextNode = nextNode.next
    currentNode.next = nextNode

    return lst