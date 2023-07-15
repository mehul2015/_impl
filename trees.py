from typing import List, Optional,Tuple

class TreeNode:
    def __init__(self, data: Optional[int] = None, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self.root = root
    
    def construct(self,nums : List[int]) -> Optional["TreeNode"]:
        return TreeNode()


    #Traversals

    def inOrder(self) -> List[int]:
        return []

    def preOrder(self) -> List[int]:
        return []

    def postOrder(self) -> List[int]:
        return []

    def levelOrder(self) -> List[int]:
        return []

    # Utility functions
    
    def size (self) -> int :
        return 0
    
    def height(self) -> int:
        return 0
    
    def maxDepth(self) -> int:
        return 0
    
    def diameter(self) -> int:
        return 0
    
    def max(self) -> int:
        return 0
    
    def min(self) -> int:
        return 0
    
    def sum(self) -> int:
        return 0
    
    #Advanced functionality

    #Alternative views

    def leftView(self) -> List[int]:
        return []
    
    def rightView(self) -> List[int]:
        return []
    
    def topView(self) -> List[int]:
        return []
    
    def bottomView(self) -> List[int]:
        return []
    
    #New Tree that answers a lot of leetcode possibilities

    def invert(self) -> Optional["TreeNode"]:
        return TreeNode()
    
    def isSymmetric(self) -> bool :
        return False

    def isBalanced(self) -> bool:
        return False
    
    def isBST(self) -> bool:
        return False
    
    def pathSum(self, target : int) -> Tuple[bool,List[int]]:
        return True,[]
    

    

    
    

