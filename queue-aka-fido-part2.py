'''
TZVM163 Cisco: Python programming (OpenEDG)
3.2.1.16 Queue aka FIFO: part 2
Student Name: Caroline Lau Campbell
'''

'''
Your task is to slightly extend the Queue class' capabilities. We want 
it to have a parameterless method that returns True if the queue is 
empty and False otherwise.

Complete the code we've provided in the editor. 
Run it to check whether its output is similar to ours.
'''

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.stack = []

    def put(self, elem):
        self.stack.insert(0,elem)

    def get(self):
        if self.stack==[]:
            raise QueueError
        else:
            foo = self.stack[-1]
            del self.stack[-1]
            return foo

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        if self.stack==[]:
            return True
        else:
            return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

'''
#############
# Test data #
#############
1
dog
False
Queue empty
'''
