def heapifyDown(i):
    
    global curr_size,heap
    
    smallest = i
    left,right = (2 * i) + 1, (2 * i) + 2

    
    if left < curr_size and heap[left] < heap[smallest]:
        smallest = left
    
    if right < curr_size and heap[right] < heap[smallest]:
        smallest = right
    
    if smallest != i:
        heap[smallest],heap[i] = heap[i],heap[smallest]
        heapifyDown(smallest)

def heapifyUp(i):
    
    global curr_size,heap
    
    p = (i - 1) // 2
    
    while p >= 0 and heap[p] > heap[i]:

        heap[i],heap[p] = heap[p],heap[i]
        i,p = p,(p - 1) // 2
    
def insertKey (x):
    
    global curr_size,heap
    
    heap[curr_size] = x
    curr_size+=1
    
    heapifyUp(curr_size-1)

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size,heap
    
    if i >= curr_size : return -1
    
    heap[i] = float("-inf")
    heapifyUp(i)
    extractMin()
    
#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    
    global curr_size,heap
    
    if curr_size <= 0 : return -1
    
    heap[0],heap[curr_size - 1] = heap[curr_size - 1],heap[0]
    r = heap[curr_size - 1]
    curr_size-=1

    heapifyDown(0)
    
    return r


# MAX HEAP


def heapify(self,arr, n, i):
        # code here
        
        largest = i
        left,right = (2*i) + 1,(2*i) + 2
        
        if left < n and arr[left] > arr[largest]: largest = left
        if right < n and arr[right] > arr[largest] : largest = right
        
        if i != largest:
            arr[largest],arr[i] = arr[i],arr[largest]
            self.heapify(arr,n,largest)
        
    
    #Function to build a Heap from array.
def buildHeap(self,arr,n):
        # code here
        
        rightMostIndex = (n - 2) // 2
        
        for i in range(rightMostIndex,-1,-1):
            self.heapify(arr,n,i)
        
    
    #Function to sort an array using Heap Sort.    
def HeapSort(self, arr, n):
        #code here
    
        self.buildHeap(arr,n)
        
        for i in range(n-1,-1,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,i,0)