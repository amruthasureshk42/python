from queue import LifoQueue
stack = LifoQueue(maxsize=3)
print("Initial size:", stack.qsize())
stack.put('M')
stack.put('N')
stack.put('O')
print("Full:",stack.full())
print("Size:",stack.qsize())
print('\n Elements popped from the stack:')
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty: ",stack.empty())


