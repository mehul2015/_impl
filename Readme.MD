# Project Documentation

🌳 This repository contains various modules for different data structures, including `Queues`, `Stacks`, `Trees` and `Utils`. Each module provides implementations and functionalities for the respective data structure.


<!-- - The `Graphs` directory contains the `graphs.py` module, which provides implementations and functionalities related to graph data structures.
- The `Linked List` directory contains the `linked-list.py` module, which provides implementations and functionalities related to linked list data structures. -->
- The `Queues` directory contains the `queues.py` module, which provides implementations and functionalities related to queue data structures.
- The `Stacks` directory contains the `stacks.py` module, which provides implementations and functionalities related to stack data structures.
- The `Trees` directory contains the `trees.py` module, which provides implementations and functionalities related to binary tree data structures.
<!-- - The `Tries` directory contains the `tries.py` module, which provides implementations and functionalities related to trie data structures. -->
- The `Utils` directory contains the `utils.py` module, which provides utility functions that can be used across multiple data structures.

## Usage

To use any of the data structures provided in this repository, you can import the respective module into your Python script or interactive session. Here's an example of how to import and use the `BinaryTree` class from the `trees.py` module:

```python
from Trees.trees import BinaryTree

# Create an instance of BinaryTree
my_tree = BinaryTree(log=False)

# Construct the binary tree
my_tree.construct(nums=[50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None])

# Use various functionalities of the BinaryTree class
print(my_tree.size())
print(my_tree.height())
print(my_tree.max())
print(my_tree.min())
print(my_tree.sum())
print(my_tree.contains(87))

# More functionalities are available, refer to the documentation in trees.py
```

Feel free to explore and use the other data structures in a similar manner.

## Additional Notes

- The `Readme.md` files in the `Queues`, `Stacks`, and `Trees` directories can provide additional information specific to those data structures. Feel free to update these files with relevant details as needed.
- The `__init__.py` files are included in the directories to make them Python packages. They can be empty or can include initialization code if required.

Enjoy using the provided data structures and have a great time coding! 🚀😊