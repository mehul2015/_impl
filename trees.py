from typing import List, Optional,Tuple
from stacks import Stack

class TreeNode:

    def __init__(self, data: Optional[int] = None, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:

    root : Optional[TreeNode] = None
    
    def __init__(self) -> None:
        self.root = None

      

    def construct(self, nums: List[int]) -> Optional[TreeNode] :
        stack = Stack()

        for num in nums:
           if num is None:
               if not stack.isEmpty():
                   stack.pop()
               else:
                   return "The input array is incorrect and a valid Binary Tree could not be generated!"
           else:
               new_node = TreeNode(data=num)
               if stack.isEmpty():
                   self.root = new_node
               else:
                  
                   parent_node = stack.peek()
                   if parent_node.left is not None:
                       parent_node.right = new_node
                   else:
                       parent_node.left = new_node

               stack.append(new_node)
                    
        return self.root 
        
    def display(self):

        if self.root is None :
            print("Root is None") 
            print(self.root)
            return

        print("In Order : ",self.inOrder())
        print("Pre Order : ",self.preOrder())
        print("Post Order : ",self.postOrder())

        

       

    #Traversals

    def inOrder(self) -> List[int]:
        res = []
        res = self.inOrderTraverse(self.root,res)
        return res
    
    def inOrderTraverse(self, node : TreeNode, result : List[int]):

        if node is None : return

        self.inOrderTraverse(node.left, result)
        result.append(node.data)
        self.inOrderTraverse(node.right,result)

        

    def preOrder(self) -> List[int]:
        res = []
        res = self.preOrderTraverse(self.root,res)
        return res

    def preOrderTraverse(self, node : TreeNode, result : List[int]):

        if node is None : return

        result.append(node.data)
        self.preOrderTraverse(node.left, result)
        self.preOrderTraverse(node.right,result)

    def postOrder(self) -> List[int]:
        res = []
        res = self.postOrderTraverse(self.root,res)
        return res

    def postOrderTraverse(self, node : TreeNode, result : List[int]):

        if node is None : return
        

        self.postOrderTraverse(node.left, result)
        self.postOrderTraverse(node.right,result)
        result.append(node.data)

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
    

    

    
    

my_tree = BinaryTree()
my_tree_root = my_tree.construct(nums=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None])
print(my_tree_root)
