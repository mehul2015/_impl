# Queue Documentation

📚 Welcome to the documentation for the `Queue` class! This class represents a queue data structure and provides various operations for working with queues.

## Class Overview

The `Queue` class is a simple implementation of a queue data structure using a Python list. It supports common queue operations such as enqueueing elements into the queue, dequeuing elements from the queue, getting the size of the queue, and checking if the queue is empty.

## Constructor

### `__init__(self)`

- Initializes a new instance of the `Queue` class.
- Returns: None.

## Operations

### Enqueue

### `enqueue(self, value) -> None`

- Adds an element to the back of the queue.
- Parameters:
  - `value`: The element to be added to the queue.
- Returns: None.

### Dequeue

### `dequeue(self)`

- Removes and returns the front element from the queue.
- Returns: The element that was dequeued from the queue, or an error message if the queue is empty.

### Is Empty

### `isEmpty(self)`

- Checks if the queue is empty.
- Returns: `True` if the queue is empty, `False` otherwise.

### Size

### `size(self)`

- Returns the number of elements in the queue.
- Returns: The size of the queue.

### Peek

### `peek(self)`

- Returns the front element of the queue without removing it.
- Returns: The front element of the queue, or an error message if the queue is empty.

This concludes the documentation for the `Queue` class. Have fun using the queue operations to manage your data effectively! 📚😊