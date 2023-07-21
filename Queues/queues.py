class Queue:

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self,value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return "There are no elements in the queue to be dequeued!"
        element_to_be_popped = self.queue[0]
        self.queue = self.queue[1:]
        return element_to_be_popped
    
    def isEmpty(self) -> bool:
        return self.size() <= 0 

    def size(self) -> int:
        return len(self.queue)
    
    def peek(self):
        if self.isEmpty():
            return "There are no elements in the queue to be peeked!"
        return self.queue[0]
        
    def sort(self):
        q = sorted(self.queu)

