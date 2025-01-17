# Node class to represent each element in the stack
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Stack class to manage stack operations
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # Add an item to the stack
    def push(self, value):
        new_1 = Node(value)
        if self.head:
            new_1.next = self.head
        self.head = new_1
        self.size += 1

    # Remove and return the top item
    def pop(self):
        # Condition to check if stack is empty
        if self.isEmpty():
            return "Stack is empty"
        pop_node = self.head
        self.head = self.head.next
        self.size -= 1
        return pop_node.value

    # Return the top item without removing it
    def peek(self):
        # Condition to check if stack is empty
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the current stack size
    def stackSize(self):
        return self.size

    # Display the entire stack
    def displayStack(self):
        # Condition to check if stack is empty
        if self.isEmpty():
            print("Stack is empty")
            return
        current = self.head
        # Traverse and print each item in the stack
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# Create a stack and test the methods
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", end="")
myStack.displayStack()  # Use displayStack to show the stack

print("Pop: ", myStack.pop())  # Pop and show top item
print("Peek: ", myStack.peek())  # Show top item without removing it
print("isEmpty: ", myStack.isEmpty())  # Check if stack is empty
print("Size: ", myStack.stackSize())  # Show current stack size
#<3