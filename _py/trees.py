from typing import List, Optional,Tuple

from stacks import Stack
from utils import Pair


class TreeNode:

    def __init__(self, data: Optional[int] = None) -> None:
        self.data = data
        self.left = None
        self.right = None



class BinaryTree:
    
    def __init__(self,log : bool) -> None:
        self.root = None
        self.log = log

    def construct(self, nums: List[int]) -> Optional[TreeNode] :

        if len(nums) == 0: return None
        if len(nums) == 1 : return nums[0]

        stack = Stack()

        root = Pair(node=TreeNode(nums[0]),count=1)
        index = 0

        stack.append(root)

        while(not stack.isEmpty()):

            top = stack.peek()

            if top.count == 1:
                index+=1
                if nums[index]:
                    new_node = TreeNode(data=nums[index]) 
                    top.node.left = new_node
                    stack.append(Pair(node=new_node,count=1))
                else:
                    top.node.left=None

                top.count+=1

            elif top.count == 2:
                index+=1
                if nums[index]:
                    new_node = TreeNode(data=nums[index]) 
                    top.node.right = new_node
                    stack.append(Pair(node=new_node,count=1))
                else:
                    top.node.right=None

                top.count+=1

            else: stack.pop()

            # if self.log:
                # print("Stack Details : ",stack.stack)
            
            self.root = root.node
        return self.root 
        
    def display(self):

        if self.root is None :
            if self.log:
                print("Root is None!")
            return

        self.inOrder()
        self.preOrder()
        self.postOrder()

    def insert(self, value : int):
        print("Inserted")
    
    def contains(self, value : int) -> bool:
        return False
    
    def delete(self,value : int):
        print("Deleted")

       

    #Traversals

    def inOrder(self) -> List[int]:

        res = []
        
        def inOrderTraverse(node : TreeNode, result : List[int]):

            if node is None : return

            inOrderTraverse(node.left, result)
            result.append(node.data)
            inOrderTraverse(node.right,result)

        inOrderTraverse(self.root,res)
        print("In Order : ",res)

        return res
    
    def preOrder(self) -> List[int]:

        res = []

        def preOrderTraverse(node : TreeNode, result : List[int]):

            if node is None : return

            result.append(node.data)
            preOrderTraverse(node.left, result)
            preOrderTraverse(node.right,result)

        preOrderTraverse(self.root,res)
        print("Pre Order : ", res)
        return res

    def postOrder(self) -> List[int]:

        res = []

        def postOrderTraverse(node : TreeNode, result : List[int]):

            if node is None : return
        

            postOrderTraverse(node.left, result)
            postOrderTraverse(node.right,result)
            result.append(node.data)

        postOrderTraverse(self.root,res)
        print("Pre Order : ", res)
        return res

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
    
    #Additional utilities

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
    


my_tree = BinaryTree(log=True)
my_tree.construct(nums=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None])
my_tree.display()



