class Stack:
    def __init__(self):
        self.list = []
        self.top = -1

    def push(self, data):
        self.data = data
        self.list.append(self.data)
        self.top = len(self.list)-1

    def pop(self):
        if (self.top == -1):
            print("Stack is empty")
            return
        data = self.list.pop()
        self.top = len(self.list)-1
        return data

    def getTOP(self):
        if(self.top == -1):
            print("Stack is empty")
            return
        return self.list[self.top]


mystack = Stack()
ans = 'Y'
while(ans == 'Y' or ans == 'yes' or ans == 'Yes' or ans == 'y'):
    choice = input("Select choice \n 1. Push to stack \n 2. Pop from stack \n 3. get top element \n ")
    if(choice == '1'):
        data = input("Enter the data you need to add \n")
        mystack.push(data)
        print("Element has pushed")
    elif(choice == '2'):
        element = mystack.pop()
        print("Element popped from the stack is " + str(element))
    elif(choice == '3'):
        print(mystack.getTOP())
    else:
        print("Enter valid option and try again")
    ans = input("Do you need to perform operation again?(yes or no)")
