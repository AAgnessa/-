import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((600, 400))
rect = pygame.Rect(10, 10, 50, 50)
#pygame.draw.rect(screen, (255, 255, 255), r, 0)


#Функция для чтения данных из файла
def funcForRead(name_fale):
    arrayWithHist = []

    try:
        file = open(name_fale, 'r')
    except:
        print("Sistem error, file not open")
    with file:
        lines = file.readlines()
        for line in lines:
            lst = eval(line) # Преобразование строки в числовой формат
            arrayWithHist.append(lst)
    
    return arrayWithHist
Array=funcForRead("Practical\data.txt")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for i in Array:
            if i==1:
                rect.move_ip(40, 0)#если цифра 1 то направо
            elif i==2:
                rect.move_ip(-40, 0)#если цифра 2 то налево
            elif i==3:
                rect.move_ip(0, 40)#если цифра 3 то вниз
            elif i==4:
                rect.move_ip(0, -40) #если цифра 4 то наверх

    pygame.draw.rect(screen, (255, 255, 255), rect, 0)
    pygame.display.flip()