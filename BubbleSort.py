import random


def bubbleSort(list):


    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]

    return list
mylist = random.sample(range(1, 40), 10)

print(mylist)

print(bubbleSort(mylist))