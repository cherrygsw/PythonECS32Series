class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)

def postfixEval(expr):
    numbers = Stack() 
    for symbol in expr:
        if symbol not in "+-*/": # Check for non-operator
            numbers.push(float(symbol)) # Convert to float and push
        else:
            if numbers.size() < 2: # Ensure two operands are available
                print("Error: insufficient values in expression")
                return None
            second = numbers.pop() # 'second' operand
            first = numbers.pop() # 'first' operand
            if symbol == '+':
                numbers.push(first + second) # Addition
            elif symbol == '-':
                numbers.push(first - second) # Subtraction
            elif symbol == '*':
                numbers.push(first * second) # Multiplication
            elif symbol == '/':
                numbers.push(first / second) # Division
    return numbers.pop() # Return result

def validParentheses(s):
    paren = Stack()
    pairs = {")": "(", "}": "{", "]": "["}
    for bracket in s: 
        if bracket in pairs.values():
            paren.push(bracket) # Push opening brackets
        elif bracket in pairs:
            if paren.isEmpty() or paren.pop() != pairs[bracket]:
                return False # Mismatch or unbalanced
    return paren.isEmpty() # Check if all are balanced

def reverseString(s):
    characters = Stack() 
    for char in s:
        characters.push(char) # Push each character
    reversedStr = ""
    while not characters.isEmpty():
        reversedStr += characters.pop() # Concatenate in reverse order
    return reversedStr # Return the reversed string