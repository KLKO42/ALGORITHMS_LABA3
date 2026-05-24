class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def check_brackets(sentence: str) -> bool:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    
    stack = Stack()
    for ch in sentence:
        if ch in '([{<':
            stack.push(ch)
        elif ch in ')]}>':
            if stack.is_empty():
                return False
            if stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()

print("МИНИ-ДЕОМНСТРАЦИЯ:")
print(check_brackets("()[]{}"))   # True
print(check_brackets("([{}])"))   # True
print(check_brackets("([)]"))     # False
print(check_brackets("<html></html>"))  # True
print(check_brackets("(a+b)*[c-d]"))    # True
