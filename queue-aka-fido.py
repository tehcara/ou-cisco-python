'''
TZVM163 Cisco: Python programming (OpenEDG)
3.2.1.15 LAB: Queue aka FIFO
Student Name: Caroline Lau Campbell
'''

'''
As you already know, a stack is a data structure realizing the LIFO 
(Last In – First Out) model. It's easy and you've already grown perfectly 
accustomed to it.

Let's try something new now. A queue is a data model characterized by the 
term FIFO: First In – First Out. Note: a regular queue (line) you know 
from shops or post offices works exactly in the same way – a customer 
who came first is served first too.

Your task is to implement the Queue class with two basic operations:
- put(element), which puts an element at end of the queue;
- get(), which takes an element from the front of the queue and returns it 
as the result (the queue cannot be empty to successfully perform it.)

Follow the hints:
- use a list as your storage (just like we did with the stack)
- put() should append elements to the beginning of the list, while get() 
should remove the elements from the end of the list;
- define a new exception named QueueError (choose an exception to derive 
it from) and raise it when get() tries to operate on an empty list.

Complete the code we've provided in the editor. 
Run it to check whether its output is similar to ours.
'''

class QueueError(IndexError):  # Choose base class for the new exception.
    print('Oh no! get() operating on empty list.')

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

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

'''
#############
# Test data #
#############
1
dog
False
Queue error
'''
