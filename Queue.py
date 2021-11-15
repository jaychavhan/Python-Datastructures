class Queue:
    def __init__(self):
        self.qlist = []
    
    def enqueue(self,data):
        self.data = data
        self.qlist.append(self.data)

    def dequeue(self):
        self.qlist.pop(0)

    def display(self):
        str = " "
        print(str.join(self.qlist))

    def getLast(self):
        print(self.qlist[len(self.qlist)-1])

    def getFirst(self):
        print(self.qlist[0])

myqueue = Queue()
ans = 'Y'
while(ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'y'):
    choice = input("Select choice \n 1. add to queue \n 2. remove from queue \n 3. get First element in queue \n 4. get Last element in queue \n 5. print queue \n ")
    if(choice == '1'):
        data = input("Enter the data you need to add \n")
        myqueue.enqueue(data)
        myqueue.display()
    elif(choice == '2'):
        myqueue.dequeue()
        myqueue.display()
    elif(choice == '3'):
        myqueue.getFirst()
    elif(choice == '4'):
        myqueue.getLast()
    elif(choice == '5'):
        myqueue.display()
    else:
        print("Enter valid option and try again")
    ans = input("Do you need to perform operation again?(yes or no)")