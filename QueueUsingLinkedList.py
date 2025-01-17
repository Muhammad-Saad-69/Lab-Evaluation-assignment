# Node class to represent each element in the queue
class Node:
    # Constructor initializing the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class to manage queue operations
class Queue:
    # Constructor initializing the queue with front, rear, and length
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    # Add an item to the queue
    def enqueue(self, element):
        new_1 = Node(element)
        if self.rear is None:
            self.front = self.rear = new_1
            self.length += 1
            return
        self.rear.next = new_1
        self.rear = new_1
        self.length += 1
    
    # Remove and return the front item
    def dequeue(self):
        # Condition to check if queue is empty
        if self.isEmpty():
            return "Queue is empty"
        temporary = self.front
        self.front = temporary.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temporary.data
    
    # Return the front item without removing it
    def peek(self):
        # Condition to check if queue is empty
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    # Check if the queue is empty
    def isEmpty(self):
        return self.length == 0
    
    # Get the current queue size
    def size(self):
        return self.length
    
    # Display the entire queue
    def displayQueue(self):
        # Condition to check if queue is empty
        if self.isEmpty():
            print("Queue is empty")
            return
        temporary = self.front
        # Traverse and print each item in the queue
        while temporary:
            print(temporary.data, end=" ")
            temporary = temporary.next
        print()

# Create a queue and test the methods
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")

myQueue.displayQueue()  # Use displayQueue to show the queue

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())