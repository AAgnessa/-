import cv2 
import numpy as np
from customtkinter import *
from PIL import Image, ImageTk

#Создание окна и определение его паррамтеров
app=CTk()#Создание окна
app.geometry(f"{600}x{500}")#Обозначение размеров
app.title("Window")#Название окна
app.configure(fg_color='pink')#Цвет бекграунда
#Считывания сигнала с видеокамеры и расположение его в окне
video=CTkLabel(master=app)
video.pack()
capture=cv2.VideoCapture(0)
    
#Чтене видео, запись его как массива данных, чтение и отображение, обновление 
while (True):
    ret, frame=capture.read()
    img=Image.fromarray(frame)
    imgtk=ImageTk.PhotoImage(image=img)
    video.config(image=imgtk)
    app.update()
   

    





    