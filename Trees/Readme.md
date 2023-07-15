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
  - [Advanced Functionality](#advanced-functionality)
    - [Alternative Views](#alternative-views)
      - [Left View](#left-view)
    - [`leftView(self) -> List[int]`](#leftviewself---listint)
      - [Right View](#right-view)
    - [`rightView(self) -> List[int]`](#rightviewself---listint)
      - [Top View](#top-view)
    - [`topView(self) -> List[int]`](#topviewself---listint)
      - [Bottom View](#bottom-view)
    - [`bottomView(self) -> List[int]`](#bottomviewself---listint)
    - [Additional Utilities](#additional-utilities)
      - [Invert](#invert)
    - [`invert(self) -> Optional[TreeNode]`](#invertself---optionaltreenode)
      - [Symmetry Check](#symmetry-check)
    - [`isSymmetric(self) -> bool`](#issymmetricself---bool)
      - [Balanced Check](#balanced-check)
    - [`isBalanced(self) -> bool`](#isbalancedself---bool)
      - [Binary Search Tree Check](#binary-search-tree-check)
    - [`isBST(self) -> bool`](#isbstself---bool)
      - [Path Sum](#path-sum)
    - [\`](#)

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

## Advanced Functionality

### Alternative Views

#### Left View

### `leftView(self) -> List[int]`

- Retrieves the left view of the binary tree, which is a list of values representing the leftmost nodes at each level of the tree.
- Returns: A list of values representing the left view of the tree.

#### Right View

### `rightView(self) -> List[int]`

- Retrieves the right view of the binary tree, which is a list of values representing the rightmost nodes at each level of the tree.
- Returns: A list of values representing the right view of the tree.

#### Top View

### `topView(self) -> List[int]`

- Retrieves the top view of the binary tree, which is a list of values representing the nodes visible from the top when looking from the vertical top-down direction.
- Returns: A list of values representing the top view of the tree.

#### Bottom View

### `bottomView(self) -> List[int]`

- Retrieves the bottom view of the binary tree, which is a list of values representing the nodes visible from the bottom when looking from the vertical top-down direction.
- Returns: A list of values representing the bottom view of the tree.

### Additional Utilities

#### Invert

### `invert(self) -> Optional[TreeNode]`

- Creates a new binary tree by inverting the left and right children of each node in the original tree.
- Returns: The root node of the inverted binary tree.

#### Symmetry Check

### `isSymmetric(self) -> bool`

- Checks whether the binary tree is symmetric, meaning that it is a mirror reflection of itself.
- Returns: `True` if the tree is symmetric, `False` otherwise.

#### Balanced Check

### `isBalanced(self) -> bool`

- Checks whether the binary tree is balanced, meaning that the heights of its left and right subtrees differ by at most one.
- Returns: `True` if the tree is balanced, `False` otherwise.

#### Binary Search Tree Check

### `isBST(self) -> bool`

- Checks whether the binary tree satisfies the binary search tree (BST) property, which states that for every node, the values in its left subtree are less than the node's value, and the values in its right subtree are greater.
- Returns: `True` if the tree is a valid binary search tree, `False` otherwise.

#### Path Sum

### `

pathSum(self, target: int) -> Tuple[bool, List[int]]`

- Finds a path in the binary tree that sums up to the given target value.
- Parameters:
  - `target` (int): The target value to find the path sum for.
- Returns: A tuple containing a boolean indicating whether a path sum was found (`True` if found, `False` otherwise), and a list of values representing the path from the root to a leaf node that sums up to the target.

This concludes the documentation for the `BinaryTree` class. Have fun exploring and using the features of this class! 🌳😊