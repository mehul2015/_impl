import sys
from typing import List, Optional,Tuple
import time


sys.path.append("/Users/mehulchattopadhyay/Desktop/_L/sys")

from Stacks.stacks import Stack
from Utils.utils import Pair,print_elapsed_time
from Queues.queues import Queue

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
        self.levelOrder()

    def contains(self, value : int) -> bool:
        start = time.time()
        if self.root is None : return False
        if self.root.data == value : return True

        def traverse(node : TreeNode,value : int) -> bool:

            if not node : return False

            if node.data == value : 
               return True
            
            return (traverse(node.left,value) if node.left else False) or (traverse(node.right,value) if node.right else False)
        if self.log:
            print_elapsed_time(task_name="Contains",start_time=start)
            
        return traverse(self.root,value)


    #Traversals

    def inOrder(self) -> List[int]:
        start = time.time()
        res = []
        
        def traverse(node : TreeNode, result : List[int]):

            if node is None : return

            if node.left : traverse(node.left, result)
            result.append(node.data)
            if node.right : traverse(node.right,result)

        traverse(self.root,res)
        print("")
        print("In Order : ",res)
        if self.log:
            print_elapsed_time(task_name="In Order Traversal",start_time=start)

        return res
    
    def preOrder(self) -> List[int]:
        start = time.time()
        res = []

        def traverse(node : TreeNode, result : List[int]):

            if node is None : return

            result.append(node.data)
            if node.left : traverse(node.left, result)
            if node.right : traverse(node.right,result)

        traverse(self.root,res)
        print("")
        print("Pre Order : ", res)

        if self.log:
            print_elapsed_time(task_name="Pre Order Traversal",start_time=start)

        return res

    def postOrder(self) -> List[int]:
        start = time.time()

        res = []

        def traverse(node : TreeNode, result : List[int]):

            if node is None : return
        

            if node.left : traverse(node.left, result)
            if node.right : traverse(node.right,result)
            result.append(node.data)

        traverse(self.root,res)
        print("")
        print("Post Order : ", res)

        if self.log:
            print_elapsed_time(task_name="Post Order Traversal",start_time=start)

        return res

    def levelOrder(self) -> List[List[int]]:

        start = time.time()
        if self.root is None : return []
        result = []
        queue = Queue()

        queue.enqueue(self.root)

        
        while(not queue.isEmpty()):
            current_level = []
            for _ in range(queue.size()):
                current_node = queue.dequeue()
                current_level.append(current_node.data)

                if current_node.left : queue.enqueue(current_node.left)
                if current_node.right : queue.enqueue(current_node.right)
            
            result.append(current_level)
        

        print("")
        print("Level Order : ")
        print("")
        for index,nodes in enumerate(result):
            print(f" Level {index + 1} :",nodes)
       
        if self.log:
     
            print_elapsed_time(task_name="Post Order Traversal",start_time=start)
        print("")
        return result


    # Utility functions
    
    def size (self) -> int :
        start = time.time()

        def size_(node : TreeNode) -> int:
            
            if node is None : return 0
            return 1 + size_(node.left) + size_(node.right)
        
        if self.log:
            print_elapsed_time(task_name="Size",start_time=start)

        return size_(self.root)
    
    #Defaults to using edges as the parameter for calculating height unless specified as nodes = True
    def height(self,nodes : bool | None = False) -> int:
       start = time.time()

       def height_(node:TreeNode,nodes : bool):
           
           if node is None :
               if nodes: return 0
               else : return -1

           return 1 + max(height_(node.left,nodes),height_(node.right,nodes))
       
       if self.log:
            print_elapsed_time(task_name="Height",start_time=start)
       return height_(self.root,nodes)
    
    #TODO
    def diameter(self) -> int:
        return 0
    
    def max(self) -> int:
        start = time.time()

        def max_(node : TreeNode) -> int :

            if node is None : return float("-inf")
            
            return max(node.data, max_(node.left),max_(node.right))
        if self.log:
            print_elapsed_time(task_name="Max",start_time=start)
        return max_(self.root)
    
    def min(self) -> int:
        start = time.time()        
        def min_(node : TreeNode) -> int :

            if node is None : return float("inf")
            
            return min(node.data, min_(node.left),min_(node.right))
        if self.log:
            print_elapsed_time(task_name="Min",start_time=start)
        return min_(self.root)
    
    def sum(self) -> int:

        start = time.time()
        def sum_(node : TreeNode):
            if node is None : return 0

            return node.data + sum_(node.left) + sum_(node.right)
        if self.log:
            print_elapsed_time(task_name="Sum",start_time=start)
        return sum_(self.root)    
    
    #TODO
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

    def invert(self) -> Optional[TreeNode]:
        return TreeNode()
    
    def isSymmetric(self) -> bool :
        return False

    def isBalanced(self) -> bool:
        return False
    
    def isBST(self) -> bool:

        start = time.time()

        def isBST_(node : TreeNode,min : int, max : int) -> bool:

            if node is None : return True

            if node.data <= min or node.data >= max : return False

            return isBST_(node.left,min,node.data) and isBST_(node.right,node.data,max)

        
        if self.log:
            print_elapsed_time(task_name="IS BST",start_time=start)
        
        return isBST_(node = self.root,min = float("-inf"),max=float("inf"))
    
    def pathSum(self, target : int) -> Tuple[bool,List[int]]:
        return True,[]
    


my_tree = BinaryTree(log=True)
my_tree.construct(nums=[50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None])
# my_tree.construct(nums=[1,2,None,None,3,None,None])

print("Size : ",my_tree.size(),end='\n\n')
print("Height :", my_tree.height(),end='\n\n')
print("Max Value in tree : ",my_tree.max(),end='\n\n')
print("Min Value in tree : ",my_tree.min(),end='\n\n')
print("Sum of nodes : ",my_tree.sum(),end='\n\n')
print("Tree Contains given value : ",my_tree.contains(345),end='\n\n')
print("Given tree is BST : ",my_tree.isBST(),end='\n\n')






