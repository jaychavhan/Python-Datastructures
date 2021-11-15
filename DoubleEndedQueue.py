class Queue:
    def __init__(self):
        self.qlist = []

    def addRear(self, data):
        self.data = data
        self.qlist.append(self.data)

    def popFront(self):
        self.qlist.pop(0)

    def addFront(self, data):
        self.data = data
        self.qlist.insert(0,self.data)
    def popRear(self):
        self.qlist.pop()
    def display(self):
        str = " "
        print(str.join(self.qlist))

    def getLast(self):
        print(self.qlist[len(self.qlist) - 1])

    def getFirst(self):
        print(self.qlist[0])


myqueue = Queue()
ans = 'Y'
while (ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'y'):
    choice = input(
        "Select choice \n 1. add to Rear \n 2. remove from Front \n 3. add to Front \n 4. remove from Rear \n 5. print queue \n ")
    if (choice == '1'):
        data = input("Enter the data you need to add \n")
        myqueue.addRear(data)
        myqueue.display()
    elif (choice == '2'):
        myqueue.popFront()
        myqueue.display()
    elif (choice == '3'):
        data = input("Enter the data you need to add \n")
        myqueue.addFront(data)
        myqueue.display()
    elif (choice == '4'):
        myqueue.popRear()
        myqueue.display()
    elif (choice == '5'):
        myqueue.display()
    else:
        print("Enter valid option and try again")
    ans = input("Do you need to perform operation again?(yes or no)")