import random

# class  NNClassifier():

#     def analyse(self, newData):


class clA():
    def __init__(self,data,name):
        self.data=data
        self.name=name

class clB():
    def __init__(self,data,name):
        self.data=data
        self.name=name       

def funcForNewObj():
    data1=[]
    #создаем несколько объектов одного класса
    for i in 'abcde':   #Цикл для создания объектов
        for j in range(10): #Цикл для создания элементов в объекте
            data1.append(random.randint(1,10))
