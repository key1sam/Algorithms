#!/usr/bin/env python
# coding: utf-8

# In[26]:


from collections import deque

class Node :
    def __init__(self, data) :
        self.data = data
        self.leftchild = None
        self.rightchild = None
        
class BinaryTree :
    def __init__(self) :
        self.root = None
    
    def preorder(self, root) :
        if root != None :
            print(root.data, end = ' ')
            self.preorder(root.leftchild)
            self.preorder(root.rightchild)
            
    def inorder(self, root) :
        if root != None :
            self.inorder(root.leftchild)
            print(root.data, end = ' ')
            self.inorder(root.rightchild)
        
    def postorder(self, root) :
        if root != None :
            self.postorder(root.leftchild)
            self.postorder(root.rightchild)
            print(root.data, end = ' ')
            
    def levelorder(self, root) :
        queue = deque()
        queue.append(root)
        while queue :
            node = queue.popleft()
            print(node.data, end = ' ')
            if node.leftchild != None :
                queue.append(node.leftchild)
            if node.rightchild != None :
                queue.append(node.rightchild)
    
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

Tree = BinaryTree()
Tree.root = n1
n1.leftchild = n2
n1.rightchild = n3
n2.leftchild = n4
n2.rightchild = n5
n3.leftchild = n6
n3.rightchild = n7

print('전위 순회')
Tree.preorder(Tree.root)
print('\n')

print('중위 순회')
Tree.inorder(Tree.root)
print('\n')

print('후위 순회')
Tree.postorder(Tree.root)
print('\n')

print('레벨 순회')
Tree.levelorder(Tree.root)

