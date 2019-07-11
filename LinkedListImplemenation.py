# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:59:08 2019

@author: paprasad
"""



#Implementation  the Nodes of the linked list, each node will have data and next pointer
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
#Linked List         
class LinkedList:
    def __init__(self):
        self.head = None
    

    #This method finds the last node of the Linked List 
    def findLastNode(self):
        temp = self.head
        while(temp):
            if(temp.next is None):
                return temp
            else:
                temp = temp.next 
        
    #Insert at the beginnning of Linked List 
    def push(self,data):
        node_head = Node(data)
        node_head.next = self.head
        self.head = node_head
        print('\nNode ',data,' added!\n')
    
    #Insert in the end of the Linked List 
    def insertEnd(self,data):
        #find the last node
        lastNode = self.findLastNode()
        newLastNode = Node(data)
        lastNode.next = newLastNode
        
     #Insert after a given Node   
    def InsertAfter(self,posNode,data):
        if posNode is None:
            print('Invalid Node - Node not in Linked In')
            return
        else:
            new_node = Node(data)
            new_node.next = posNode.next
            posNode.next = new_node  
    
    def deleteNode(self,data):
        temp  = self.head
        found_flag = False 
        if temp.data == data:
            self.head = temp.next
            temp = None
            return
        prev = Node(None)
        while(temp is not None):
            if temp.data == data:
                prev.next = temp.next
                temp = prev
                found_flag = True
            prev = temp
            temp = temp.next
        
        if found_flag is False:
            print('No Node ',data,' found in the Linked List\n')
    
    def positionalDelete(self, position):
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            print('Deleted the Node at head position')
            return 
        else:
            for i in range(position-1):
                temp = temp.next
                if temp is None:
                    break
                
                
            if temp is None or temp.next is None:
                print('Given position is greater than Linked List length')
                return
            else:
               temp.next = temp.next.next
                
                
                
                
     #Method to print the Linked List   
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
        
        
if __name__ == '__main__':
    list = LinkedList()
    node_1 = Node(25)
    node_2 = Node(22)
    node_3 = Node(26)
    list.head = node_1
    list.head.next = node_2
    node_2.next = node_3
    print('----------------Linked List element-------------------\n\n')
    list.printList() 
    list.push(30)
    print('\n\n\n----------------Linked List modified with new head-------------------\n\n')
    list.printList() 
    list.InsertAfter(node_2,32)
    print('\n\n\n----------------Linked List modified with new node, Inserted after the given node, 32 after 22 (Node_2)-------------------\n\n')
    list.printList() 
    list.insertEnd(99)
    print('\n\n\n---------------- Inserting Node 99 in the Last-------------------\n\n')
    list.printList() 
    print('\n\n\n---------------- Deleting the  Node 22-------------------\n\n')
    list.deleteNode(22)
    list.printList()
    print('\n\n\n---------------- Deleting the  Node 32-------------------\n\n')
    list.deleteNode(32)
    list.printList()
    print('\n\n\n---------------- Deleting the  head Node 30-------------------\n\n')
    list.deleteNode(30)
    list.printList()
    print('\n\n\n---------------- Deleting the Last Node 99-------------------\n\n')
    list.deleteNode(99)
    list.printList()
    print('\n\n\n---------------- Add Node 23,24,23,27,24-------------------\n\n')
    list.push(56)
    list.push(59)
    list.push(89)
    list.push(76)
    list.push(41)
    print('\n\n\n---------------- Linked list after new Nodes-------------------\n\n')
    list.printList()
    print('\n\n\n---------------- Deleting the Last Node 23 which occur multiple time-------------------\n\n')
    list.deleteNode(23)
    list.printList()
    print('\n\n\n---------------- If Node is not found in the linked list e.g 100-------------------\n\n')
    list.deleteNode(100)
    list.printList()
    print('\n\n\n---------------- Delete at position 3-------------------\n\n')
    list.positionalDelete(3)
    list.printList()
    print('\n\n\n---------------- Delete at position 1-------------------\n\n')
    list.positionalDelete(1)
    list.printList()
    print('\n\n\n---------------- Delete at position 4-------------------\n\n')
    list.positionalDelete(4)
    list.printList()
    print('\n\n\n---------------- Delete at position 0-------------------\n\n')
    list.positionalDelete(0)
    list.printList()                          
             