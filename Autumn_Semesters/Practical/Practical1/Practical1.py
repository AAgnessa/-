import math

class robot():
    def __init__(self, ipMQTT, numPort,nameTopik,speed,rotation, name_file):
        self.ipMQTT=ipMQTT
        self.numPort=numPort
        self.nameTopik=nameTopik
        self.speed=speed
        self.rotation=rotation
        self.name_file=name_file

#Функция для чтения координат из файла
def readfile(file_name):
    arr = []
    try:
        file = open(file_name, 'r')
    except:
        print("hui")
    with file:
        cords = file.readlines()
        for line in cords:
            x, y = map(int, line[:3].split(' '))
            arr.append([x, y])
    return arr

# Функция для расчета расстояния
def countDistance(arr):
    distance = []
    for i in range(len(arr)-1):
        dist = math.sqrt((arr[i][0]-arr[i+1][0])**2+(arr[i][1]-arr[i+1][1]))
        distance.append(dist)
    return distance

#Функция для расчета времени
def countTime(speed, distanse):
    time=[]
    for i in range(len(distanse)):
        time.append(distanse[i]/speed)
    return time


if __name__=='__main__':
    a=robot('10.0.2.2.', 1883, 'abotcmd1', 2.0, 30.0,'Practical\\Practical1\\XY.txt')
    f = readfile(a.name_file)
    d = countDistance(f)
    t=countTime(a.speed, d)
    print(t)

