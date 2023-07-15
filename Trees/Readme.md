# BinaryTree Documentation

🌳 Welcome to the documentation for the `BinaryTree` class! This class represents a binary tree data structure and provides various operations and functionalities for working with binary trees.

## Table of Contents

- [BinaryTree Documentation](#binarytree-documentation)
  - [Table of Contents](#table-of-contents)
  - [Class Overview](#class-overview)
  - [Constructor](#constructor)
    - [`__init__(self, log: bool)`](#__init__self-log-bool)
  - [Construction from List](#construction-from-list)
    - [`construct(self, nums: List[int]) -> Optional[TreeNode]`](#constructself-nums-listint---optionaltreenode)
  - [Displaying the Binary Tree](#displaying-the-binary-tree)
    - [`display(self)`](#displayself)
  - [Basic Operations](#basic-operations)
    - [Contains](#contains)
    - [`contains(self, value: int) -> bool`](#containsself-value-int---bool)
    - [Traversals](#traversals)
      - [In-order Traversal](#in-order-traversal)
    - [`inOrder(self) -> List[int]`](#inorderself---listint)
      - [Pre-order Traversal](#pre-order-traversal)
    - [`preOrder(self) -> List[int]`](#preorderself---listint)
      - [Post-order Traversal](#post-order-traversal)
    - [`postOrder(self) -> List[int]`](#postorderself---listint)
    - [Size](#size)
    - [`size(self) -> int`](#sizeself---int)
    - [Height](#height)
    - [`height(self) -> int`](#heightself---int)
    - [Maximum Value](#maximum-value)
    - [`max(self) -> int`](#maxself---int)
    - [Minimum Value](#minimum-value)
    - [`min(self) -> int`](#minself---int)
    - [Sum of Values](#sum-of-values)
    - [`sum(self) -> int`](#sumself---int)

## Class Overview

The `BinaryTree` class represents a binary tree data structure. It consists of nodes, where each node contains a data value and references to its left and right child nodes. The class provides methods to construct a binary tree, display its structure, perform basic operations like traversals and size/height calculations, as well as advanced functionalities like alternative views and checks for symmetry, balance, and binary search tree property.

## Constructor

### `__init__(self, log: bool)`

- Initializes a new instance of the `BinaryTree` class.
- Parameters:
  - `log` (bool): Specifies whether to enable logging during tree construction and display. If set to `True`, detailed information about the construction process will be printed.
- Returns: None.

## Construction from List

### `construct(self, nums: List[int]) -> Optional[TreeNode]`

- Constructs a binary tree from a list of numbers.
- Parameters:
  - `nums` (List[int]): The list of numbers representing the binary tree structure. The numbers are inserted in level order from left to right. Use `None` to represent a missing node.
- Returns: The root node of the constructed binary tree.

## Displaying the Binary Tree

### `display(self)`

- Displays the binary tree by performing in-order, pre-order, and post-order traversals.
- Returns: None.

## Basic Operations

### Contains

### `contains(self, value: int) -> bool`

- Checks whether the binary tree contains a specific value.
- Parameters:
  - `value` (int): The value to search for in the binary tree.
- Returns: `True` if the value is found in the tree, `False` otherwise.

### Traversals

#### In-order Traversal

### `inOrder(self) -> List[int]`

- Performs an in-order traversal of the binary tree and returns a list of node values.
- Returns: A list of node values in the order they were visited during the in-order traversal.

#### Pre-order Traversal

### `preOrder(self) -> List[int]`

- Performs a pre-order traversal of the binary tree and returns a list of node values.
- Returns: A list of node values in the order they were visited during the pre-order traversal.

#### Post-order Traversal

### `postOrder(self) -> List[int]`

- Performs a post-order traversal of the binary tree and returns a list of node values.
- Returns: A list of node values in the order they were visited during the post-order traversal.

### Size

### `size(self) -> int`

- Calculates the number of nodes in the binary tree.
- Returns: The number of nodes in the tree.

### Height

### `height(self) -> int`

- Calculates the height of the binary tree.
- Returns: The height of the tree (the maximum number of edges from the root to a leaf node).

### Maximum Value

### `max(self) -> int`

- Finds the maximum value in the binary tree.
- Returns: The maximum value present in the tree.

### Minimum Value

### `min(self) -> int`

- Finds the minimum value in the binary tree.
- Returns: The minimum value present in the tree.

### Sum of Values

### `sum(self) -> int`

- Calculates the sum of all values in the binary tree.
- Returns: The sum of all values in the tree.





This concludes the documentation for the `BinaryTree` class. Happy Coding 🌳😊
