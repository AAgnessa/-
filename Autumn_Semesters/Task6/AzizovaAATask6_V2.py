from tkinter import *
import cv2
from PIL import Image, ImageTk

window=Tk()
window.title('Hello')
window.geometry("600x500")


#Добавляем изображение
canvas = Canvas(window, height=250, width=500)#Создание холста
image = Image.open("Task6/photo.jpg")#открываем фото
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(100, 20, anchor='nw',image=photo)
canvas.grid(row=2,column=1)

    
def show_clicked(event):
        print("event: EVENT_LBUTTONDBLCLK")
        cv2.circle(image,(x, y), 20,(255,0,0), 5)


window.mainloop()