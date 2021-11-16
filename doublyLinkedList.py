class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addBeforeList(self, newdata):
        self.newdata = node(newdata)

        if(self.head == None):
            self.head = self.newdata
            self.tail = self.newdata
        else:
            self.head.prev = self.newdata
            self.newdata.next = self.head
            self.head = self.newdata
    def addAfter(self, data, newdata):
        self.data = data
        self.newdata = node(newdata)
        temp = self.head
        while(temp):
            if(temp.data == self.data):
                if(temp.next is not None):
                    temp.next.prev = self.newdata
                    self.newdata.prev = temp
                    self.newdata.next = temp.next
                    temp.next = self.newdata
                else:
                    temp.next = self.newdata
                    self.newdata.prev = temp
                    self.tail = self.newdata
            temp = temp.next
    def append(self, newdata):
        self.newdata = node(newdata)
        if(self.head == None):
            self.head = self.newdata
            self.tail = self.newdata
        else:
            self.tail.next = self.newdata
            self.newdata.prev = self.tail
            self.tail = self.newdata

    def delHead(self):
        temp = self.head
        if(self.head != self.tail):
            self.head = temp.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
    def deleteNode(self, data):
        self.data = data
        temp = self.head
        if(temp.data == self.data):
            self.delHead()
            return
        while(temp):
            if(temp.data == self.data):
                if(temp.next is not None):
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
                else:
                    self.tail = temp.prev
                    self.tail.next = None

            temp = temp.next
    def delTail(self):
        temp = self.tail
        if(self.head != self.tail):
            self.tail = temp.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None

    def printList(self):
        temp = self.head
        dll = []
        string = " "
        if(self.head == None):
            print("\n No element in Linked-list. Please try adding elements first")
            return
        while (temp):
            if(temp.next is not None):
                dll.append((str(temp.data) + "-->"))
            else:
                dll.append((str(temp.data)))
            temp = temp.next
        print(string.join(dll))

myqueue = linkedList()
ans = 'Y'
while(ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'y'):
    choice = input("Select choice \n 1. add Before List \n 2. add after specific node \n 3. append \n 4. delete head \n 5. "
                   "delete node \n 6. Delete Tail \n 7. Print Linked-list \n")
    if(choice == '1'):
        data = input("Enter the data you need to add \n")
        myqueue.addBeforeList(data)
        myqueue.printList()
    elif(choice == '2'):
        data = input("Enter previous data \n")
        newdata = input(" new data to be added after it \n")
        myqueue.addAfter(data, newdata)
        myqueue.printList()
    elif(choice == '3'):
        data = input("Enter data you need to append\n")
        myqueue.append(data)
        myqueue.printList()
    elif (choice == '4'):
        myqueue.delHead()
        myqueue.printList()
    elif (choice == '5'):
        data = input("Enter the data you want to delete\n")
        myqueue.deleteNode(data)
        myqueue.printList()
    elif (choice == '6'):
        myqueue.delTail()
        myqueue.printList()
    elif (choice == '7'):
        myqueue.printList()
    else:
        print("Enter valid option and try again")
    ans = input("Do you need to perform operation again?(yes or no)")
