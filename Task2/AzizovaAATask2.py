from math import sqrt

#Функция для построения равнобедренного треугольника 
def triangle(a):
    k=1
    for i in range(a+1):
        print(a*' ', k*'*', a*' ', sep='')
        a-=1
        k+=2
#triangle(5)


#Функция для вычисления расстояния между гистограммами
def histDistanve(hist1, hist2):
    d_sq=0
    if len(hist1)==len(hist2):
        for i in range (len(hist1)):
            d_sq+=(hist2[i]-hist1[i])**2
        print(sqrt(d_sq))
    else:
        print('Расмерность векторов гистограммы не совпадает')
#histDistanve([1,2,3],[4,5,6])

#Функции для записи гистограмм в файл
def funcForWriteHist(name_fale,writeHist):
    file = open(name_fale, "w")
    file.write(writeHist)
    file.close()

#array_one=[[1,2,3], [4,5,6], [7,8,9]] #Массив с n мерными гистограммами
#funcForWriteHist(str(array_one))

#Функция для чтения гистограмм из файла
def funcForReadHist(name_fale):
    arrayWithHist = []

    file = open(name_fale, 'r')
    lines = file.readlines()

    for line in lines:
        lst = eval(line) # Преобразование строки в числовой формат
        arrayWithHist.append(lst)
    
    file.close()
    return arrayWithHist

arrayWithHist = funcForReadHist("dataHist")

