
# http://www.shafaetsplanet.com/?p=2342

class Stack:
    def __init__(self, max_size):
        self.top_pointer = -1 
        self.stack = [None for x in range(max_size)]

    def push(self, new_element):
        self.top_pointer = self.top_pointer + 1
        self.stack[self.top_pointer] = new_element

    def pop(self):
        last_element = self.stack[self.top_pointer]
        self.top_pointer = self.top_pointer - 1
        return last_element

    def peek(self):
        return self.stack[self.top_pointer]

    def is_empty(self):
        return self.top_pointer == -1

def checkBalance(s):
    myStack = Stack(len(s))
    if s == "":
        return True

    for c in s:
        if c == "(" or c == "{":
            myStack.push(c)
        else:
            if myStack.is_empty():
                return False
            if c == ")" and myStack.peek() != "(":
                return False
            if c == "}" and myStack.peek() != "{":
                return False
            myStack.pop()
    
    if myStack.is_empty():
        return True
    return False
if __name__ == "__main__":
    result = checkBalance("(({)}))")
    print(result)
