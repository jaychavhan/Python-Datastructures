class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class linkedList:
    def __init__(self):
        self.head = None

    def addBeforeList(self, newdata):
        self.newdata = node(newdata)

        if(self.head == None):
            self.head = self.newdata
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
                temp.next.prev = self.newdata
                self.newdata.prev = temp
                self.newdata.next = temp.next
                temp.next = self.newdata
            temp = temp.next
    def append(self, newdata):
        self.newdata = node(newdata)
        if(self.head == None):
            self.head =self.newdata
        last = self.head
        while(last.next):
            last = last.next
        last.next = self.newdata
        self.newdata.prev = last

    def delHead(self):
        temp = self.head
        self.head = temp.next
        self.head.prev = None
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
                    temp.prev.next = None

            temp = temp.next

    def printList(self):
        temp = self.head
        a = []
        string = " "
        while (temp):
            a.append((str(temp.data) + "-->"))
            temp = temp.next
        print(string.join(a))

myList = linkedList()
ans = 'Y'
while(ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'y'):
    choice = input("Select choice \n 1. add Before List \n 2. add after specific node \n 3. append \n 4. delete head \n 5. delete node \n 6. print list \n")
    if(choice == '1'):
        data = input("Enter the data you need to add \n")
        myList.addBeforeList(data)
        myList.printList()
    elif(choice == '2'):
        data = input("Enter previous data \n")
        newdata = input(" new data to be added after it \n")
        myList.addAfter(data, newdata)
        myList.printList()
    elif(choice == '3'):
        data = input("Enter data you need to append\n")
        myList.append(data)
        myList.printList()
    elif (choice == '4'):
        myList.delHead()
        myList.printList()
    elif (choice == '5'):
        data = input("Enter the data you want to delete\n")
        myList.deleteNode(data)
        myList.printList()
    elif (choice == '6'):
        myList.printList()
    ans = input("Do you need to perform operation again?(yes or no)")