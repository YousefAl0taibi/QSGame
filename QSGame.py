import csv
import copy
from collections import deque
Questions={}
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
    def __init__(self,question=None,data=None):
        self.left=None
        self.right=None
        self.question=question
        self.data=data
class BST:
    def __init__(self,data:dict,question:str,attr:str,attr_value:str):
        self.root=Node(question)
        self.leavs(data,attr,attr_value)
    def leavs(self,data:dict,attr:str,attr_value:str):
        left_data={key:val for key,val in data.items() if val.get(attr)==attr_value}
        right_data={key:val for key,val in data.items() if val.get(attr)!=attr_value}
        self.root.left=Node(data=left_data)
        self.root.right=Node(data=right_data)
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
 #-----------------------------------------من هنا وتحت مو من ضمن الكود  
    def print_tree(self):
        print(f"Question: {self.root.question}")
        print("\nLeft (Yes answer):")
        for name, info in self.root.left.data.items():
            print(f"{name}: {info}")
        print("\nRight (No answer):")
        for name, info in self.root.right.data.items():
            print(f"{name}: {info}")
     
       
bst=BST(hashmap,"is the person male","Gender","Male")
bst.print_tree()
def BestQS(Hashmap):
    HashC=copy.deepcopy(Hashmap)
    


    pass
print(abs(sum(1 for d in hashmap.values() if d['Gender']=="Male")-sum(1 for d in hashmap.values() if d['Gender']=="Female")))
