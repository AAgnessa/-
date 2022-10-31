import random
import time
import math
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

#Функция заполняющая массив элементами от 0 до 999 в количестве - 1 000 000
#UPD: Универсальная функция для заполнения массива случайными элементами. countNumber-количество элементов в массиве, a,b - границы рандома.
def initListWithRandomNumbers(countNumber,a,b):
    arrayWithRandomNumber=[]
    for i in range (countNumber):
        a=random.randint(a, b)
        arrayWithRandomNumber.append(a)
    return(arrayWithRandomNumber)


#Функция перебирающая массив и считающая кол-во цифр
def counterNumber(array):
    counter=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(1000000):
        if 0<=array[j]<=99:
            counter[0]=counter[0]+1
        elif 100<=array[j]<=199:
            counter[1]=counter[1]+1
        elif 200<=array[j]<=299:
            counter[2]=counter[2]+1
        elif 300<=array[j]<=399:
            counter[3]=counter[3]+1
        elif 400<=array[j]<=499:
            counter[4]=counter[4]+1
        elif 500<=array[j]<=599:
            counter[5]=counter[5]+1
        elif 600<=array[j]<=699:
            counter[6]=counter[6]+1
        elif 700<=array[j]<=799:
            counter[7]=counter[7]+1
        elif 800<=array[j]<=899:
            counter[8]=counter[8]+1
        elif 900<=array[j]<=999:
            counter[9]=counter[9]+1
    return(counter)

#Функция счетчик времени работы программы
def timeCounter(arrayWithRandomNumber):
    finalArray=[]
    for k in range(100):
        start=time.time()
        counterNumber(arrayWithRandomNumber)
        end=time.time()
        timeWork=end-start
        finalArray.append(timeWork)
    print('Максимальное время работы программы:', max(finalArray), end='\n')
    print('Среднее время работы программы:', mean(finalArray))
    print('Минимальное время работы программы:', min(finalArray))
    return(finalArray)

#Функция для построение гистограмы частоты значения времени работы программы 
#UPD:Универсальная программа для построение гистгорамм. finalArray - массив данных необходимых для построения, name_title - название гистограммы, xб y - имя оси 
def plotHistogram(finalArray,name_title,x,y):
    #Построение гистограммы
    plt.hist(finalArray,edgecolor="black", bins =10)    
    plt.title(name_title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()    





