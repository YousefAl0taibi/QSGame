import csv
from collections import deque
def Hashmap(filename,key_column):
    hashmap={}
    with open(filename,newline='',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
            key=row[key_column]
            data={k:v for k,v in row.items() if k!=key_column}
            hashmap[key]=data
    return hashmap
filename='311CSC_Project_Dataset.csv'
keycolumn='Name'
hashmap=Hashmap(filename,keycolumn)
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,answer,key):
        if root is None:
            return Node(key)
        if answer=='Yes':
            root.left=self.insert(root.left,answer,key)
        elif answer=='No':
            root.right=self.insert(root.right,answer,key)
        else:
            print('wrong input')
        return root
    def preorder(self, root):
        if root:
            print(root.value, end=" ") 
            self.preorder(root.left)
            self.preorder(root.right)
    def level_order(self):
        if self.root is None:
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            print(current.value, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
bst=BST()
bst.root=bst.insert(bst.root,'Yes','hello')
bst.insert(bst.root,'No','how are you')
bst.insert(bst.root,'Yes','how old')
bst.insert(bst.root,'Yes','okio')
bst.level_order()