class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data
        self.next = None



class  LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


    def printList(self):

     temp = self.head
     while (temp):
         print(temp.data)
         temp = temp.next
    def push(self,newdata):
         new_node=Node(newdata)
         #self.head =new_node
         new_node.next=self.head
         self.head=new_node
    def insertafter(self,prevnode,newnode):
        if(prevnode is None):
            print("cannot return")
        node=Node(newnode)
        node.next=prevnode.next
        prevnode.next=node
    def insertafterindex(self,newdata,x):
        temp=self.head
        if(x==0):
            newnode=Node(newdata)
            newnode.next=temp.next
            self.head=newnode
        else:
            i=0
            while(i<x):
                temp=temp.next
                if(temp==None):
                    return
                i=i+1

            newnode=Node(newdata)
            newnode.next=temp.next
            temp.next=newnode





    def deletenode(self,x):
        temp=self.head
        if (temp.data==x):
            self.head=temp.next
            temp=None
            return
        while(temp!=None):
            if(temp.data==x):
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return

        prev.next=temp.next
        temp=None

    def deleteposition(self,pos):
        if(self.head==None):
            return None
        temp=self.head
        if(pos==0):
            self.head=temp.next
            temp=None
            return
        else:
            i=0
            while(i<pos-1):
                temp=temp.next
                if(temp==None):
                    return
                i=i+1
            link=temp.next.next
            temp.next=None
            temp.next=link









if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next=second
    second.next=third
    llist.printList()
    llist.push(4)
    print()
    llist.printList()
    print()
    llist.insertafter(llist.head.next,7)
    llist.printList()

    #llist.printList()
    print()
    llist.deletenode(7)
    llist.printList()
    llist.deleteposition(2)
    print()
    llist.printList()
    print()
    llist.insertafterindex(5,2)
    llist.printList()
