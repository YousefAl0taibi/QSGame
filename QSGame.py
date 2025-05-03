import csv
def generate_QS(filename,key_column): # to generate the all posible questions
    attributes_values={}
    with open(filename, newline='', encoding='utf-8') as file:
        reader=csv.DictReader(file) #read from file
        for row in reader:
            for attr,val in row.items(): #take values to make program know what should do with eache qeustion
                if attr!=key_column  and not(val=="Female" or val=="No"):
                    if attr not in attributes_values:
                        attributes_values[attr]=set()  
                    attributes_values[attr].add(val)

    questions={}
    for attr, attr_value in attributes_values.items(): #make the text question to show to the user
        for value in attr_value:
            if(value=="Yes" or value=="No"):
                question=f"Is the person's {attr}?"
            else:
                question=f"Is the person's {attr} {value}?"
            questions[question]=[attr, value]

    return questions

def Hashmap(filename,key_column):#save data in hashmap
    hashmap={}
    with open(filename,newline='',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
            key=row[key_column]
            data={k:val for k,val in row.items() if k!=key_column}
            hashmap[key]=data
    return hashmap

filename='311CSC_Project_Dataset.csv'
keycolumn='Name'
hashmap=Hashmap(filename,keycolumn)
Questions=generate_QS(filename,"Name")

class Node:#make node to each person and each question
    def __init__(self,question=None,data=None):
        self.left=None
        self.right=None
        self.question=question
        self.data=data

class BST:#make BST to run every question and person inside it
    def __init__(self,data:dict):
        self.root = Node(None,data)

    def insert(self, node,data:dict,question:str,answer:str,attr:str,attr_value:str):#insert every data in left and right
        if node is None:
            return Node(question, data)

        left_data={key:val for key,val in data.items() if val.get(attr) == attr_value}
        right_data={key:val for key,val in data.items() if val.get(attr) != attr_value}
        node.question=question
        node.left=Node(question,data=left_data)
        node.right=Node(question,data=right_data)
        if answer=="Yes":
            return (node,node.left)
        
        elif answer=="No":
            return (node,node.right)

        return node

    def build_tree(self,questions:dict):#do The game here
        print("\nWelcome to The Questions Game")
        print("\nAnswer The Questions with Yes or No to find the famous person")
        node = self.root
        questions_copy=questions.copy()
        current_data=node.data.copy()  
        questions_asked=0

        while len(current_data)>1:
            qskey=self.best_QS(questions_copy, current_data)#take the best question
            if qskey is None:
                break

            attr,attr_value=questions_copy[qskey]

            print(f"\nQuestion: {qskey}")
            user_input=input("\n(Yes/No)? \n").strip().capitalize()

            while user_input not in ["Yes", "No"]:
               user_input=input("Please enter Yes or No: ").strip().capitalize()

            questions_asked+=1
            

        
            if user_input=="Yes":
                current_data={k:val for k,val in current_data.items() if val[attr]==attr_value}

            elif user_input=="No":
                current_data={k:val for k,val in current_data.items() if val[attr]!=attr_value}

        
            questions_copy={key:val for key,val in questions_copy.items() if key!=qskey}

            parent,node=self.insert(node,node.data,qskey,user_input,attr,attr_value) #insert data to the tree
            node.data=current_data #change the pointer to the salect node
            self.print_tree(parent,node)#print the how much remaining person in left and right
        print(f"The Number of Questions Needed={questions_asked}")
        print("Best Case:6 Questions")
        print("Worst Case:50 Questions")
            
            
    def print_tree(self,node,current_node):
        if node is None:
            return
        
        if len(current_node.data)==1:
            print("\n{"+f"Final Answer: {list(current_node.data.keys())[0]}"+"}\n")
            return
        
        else:
            print("remaining names:\n")
            print(f"Yes:{len(node.left.data)}", end=" ")
            print(f"No:{len(node.right.data)}")
            print("\n")

        

    def best_QS(self,questions:dict,data:dict):#take the best question
        lst_bestQS={}
    
        for qskey,(attr,attr_value) in questions.items():
            left=sum(1 for d in data.values() if d[attr]==attr_value)
            right=sum(1 for d in data.values() if d[attr]!=attr_value)
            abs_sum=abs(left-right)

      
            if left>0 and right>0:#to take a valuable question
                lst_bestQS[qskey]=abs_sum

    
        if not lst_bestQS:
            return None

        bestQS=min(lst_bestQS, key=lst_bestQS.get)
        return bestQS
            

    



bst = BST(hashmap) #create the tree
bst.build_tree(Questions)#start the game
