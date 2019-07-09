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
    

    
    def push(self,data):
        node_head = Node(data)
        node_head.next = self.head
        self.head = node_head
        

        
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
    
             