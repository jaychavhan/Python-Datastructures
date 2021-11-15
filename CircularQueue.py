class circularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.head = -1
        self.tail = -1
        self.size = size

    def enqueue(self, data):
        self.data = data

        if((self.tail + 1) % (self.size) == self.head):
            print("Queue is full!!!")
        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = self.data
        else:
            self.tail = (self.tail + 1) % (self.size)
            self.queue[self.tail] = self.data

    def dequeue(self):

        if(self.head == -1):
            print("Queue is empty!!!")
        elif(self.head == self.tail):
            data = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return data
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            return data

    def getHead(self):
        if(self.head == -1):
            print("No element in queue")
        else:
            print(self.queue[self.head])

    def getTail(self):
        if(self.tail == -1):
            print("No element in queue")
        else:
            print(self.queue[self.tail])

    def display(self):
        if(self.head == -1):
            print("No element in queue")
        elif(self.tail >= self.head):
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.head, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail+1):
                print(self.queue[i], end=" ")

size = int(input("Enter Size of Circular queue \n"))
myqueue = circularQueue(size)
ans = 'Y'
while(ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'y'):
    choice = input("Select choice \n 1. add to queue \n 2. remove from queue \n 3. get head of queue \n 4. get tail of queue \n 5. print queue \n ")
    if(choice == '1'):
        data = input("Enter the data you need to add \n")
        myqueue.enqueue(data)
        myqueue.display()
    elif(choice == '2'):
        data = myqueue.dequeue()
        print("Dequeue element: " + str(data))
        myqueue.display()
    elif(choice == '3'):
        myqueue.getHead()
    elif(choice == '4'):
        myqueue.getTail()
    elif(choice == '5'):
        myqueue.display()
    else:
        print("\n Enter valid option and try again")
    ans = input("\n Do you need to perform operation again?(yes or no)")



