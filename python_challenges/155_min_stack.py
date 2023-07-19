class MinStack:
    def __init__(self):
        self.stack = []
        self.current_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.current_min:
            if val <= self.current_min[-1]:
                self.current_min.append(val)
        else:
            self.current_min.append(val)

    def pop(self) -> None:
        returned_val = self.stack.pop()
        if self.current_min and self.current_min[-1] == returned_val:
            self.current_min.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min[-1]


"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

min_stack = [-2, -3]

 """


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
