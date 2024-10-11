class CustomQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):

        self.queue.append(value)
        print(f"Enqueue: {value}")

    def dequeue(self):
      
        if not self.is_empty():
            value = self.queue.pop(0) 
            print(f"Dequeue: {value}")
            return value
        else:
            print("Queue is empty, so cannot dequeue.")
            return None

    def peek(self):
  
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. Nothing to peek.")
            return None

    def is_empty(self):
   
        return len(self.queue) == 0

    def size(self):
 
        return len(self.queue)

    def display(self):
 
        print("Current Queue:", self.queue)


queue = CustomQueue()


queue.enqueue(11)
queue.enqueue(22)
queue.enqueue(33)
queue.enqueue(55)
queue.enqueue(66)
queue.enqueue(77)
queue.enqueue(88)


queue.display()

#peek
print("Peek:", queue.peek())


queue.dequeue()
queue.dequeue()


queue.display()


print("Is Queue Empty?", queue.is_empty())


print("Queue Size:", queue.size())
