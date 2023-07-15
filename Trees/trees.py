import sys
from typing import List, Optional,Tuple

sys.path.append("/Users/mehulchattopadhyay/Desktop/_L/sys")

from Stacks.stacks import Stack
from Utils.utils import Pair

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
        self.display()
        return self.root 
        
    def display(self):

        if self.root is None :
            if self.log:
                print("Root is None!")
            return

        self.inOrder()
        self.preOrder()
        self.postOrder()

    def contains(self, value : int) -> bool:

        if self.root is None : return False
        if self.root.data == value : return True

        def traverse(node : TreeNode,value : int) -> bool:

            if not node : return False

            if node.data == value : 
               return True
            
            return (traverse(node.left,value) if node.left else False) or (traverse(node.right,value) if node.right else False)
            
        return traverse(self.root,value)


    #Traversals

    def inOrder(self) -> List[int]:

        res = []
        
        def traverse(node : TreeNode, result : List[int]):

            if node is None : return

            if node.left : traverse(node.left, result)
            result.append(node.data)
            if node.right : traverse(node.right,result)

        traverse(self.root,res)
        print("In Order : ",res)

        return res
    
    def preOrder(self) -> List[int]:

        res = []

        def traverse(node : TreeNode, result : List[int]):

            if node is None : return

            result.append(node.data)
            if node.left : traverse(node.left, result)
            if node.right : traverse(node.right,result)

        traverse(self.root,res)
        print("Pre Order : ", res)
        return res

    def postOrder(self) -> List[int]:

        res = []

        def traverse(node : TreeNode, result : List[int]):

            if node is None : return
        

            if node.left : traverse(node.left, result)
            if node.right : traverse(node.right,result)
            result.append(node.data)

        traverse(self.root,res)
        print("Pre Order : ", res)
        return res

    def levelOrder(self) -> List[int]:
        return []


    # Utility functions
    
    def size (self) -> int :

        def size_(node : TreeNode) -> int:
            
            if node is None : return 0
            return 1 + size_(node.left) + size_(node.right)

        return size_(self.root)
 
    def height(self) -> int:

       def height_(node:TreeNode):
           
           if node is None : return 0

           return 1 + max(height_(node.left),height_(node.right))
       
       return height_(self.root)
    
    def diameter(self) -> int:
        return 0
    
    def max(self) -> int:

        def max_(node : TreeNode) -> int :

            if node is None : return float("-inf")
            
            return max(node.data, max_(node.left),max_(node.right))
        
        return max_(self.root)
    
    def min(self) -> int:
        def traverse(node : TreeNode) -> int :

            if node is None : return float("inf")
            
            return min(node.data, traverse(node.left),traverse(node.right))
        
        return traverse(self.root)
    
    def sum(self) -> int:

        def sum_(node : TreeNode):
            if node is None : return 0

            return node.data + sum_(node.left) + sum_(node.right)
    
        return sum_(self.root)    
    
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
    


my_tree = BinaryTree(log=False)
my_tree.construct(nums=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None])

print(my_tree.size())
print(my_tree.height())
print(my_tree.max())
print(my_tree.min())
print(my_tree.sum())
print(my_tree.contains(87))






