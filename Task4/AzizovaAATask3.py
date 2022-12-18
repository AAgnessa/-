import os
import paho.mqtt.client as mqtt
#http://www.steves-internet-guide.com/into-mqtt-python-client/

#Функция для работы с терминалом. 
#На вход принимает строку.
def funcCMD(comand):
    cmd=comand
    code_exit=os.system(cmd)
    return code_exit

#Функция для счения данных из файла и публикации их в топик/
#На вход принимает название файла (STR), а так же название топика для публикации (STR)
def pubTopik(name_file, name_topik):
    try:
        file = open(name_file, 'r')
    except:
        print("Sistem error, file not open")
    with file:
        lines = file.readlines()
        for line in lines:
            funcCMD('mosquitto_pub -t'+ name_topik + '-m' + line)

#Функция для подписки на топик и чтение данных
def subTopik(name_topik):
    code_exit=[]
    i=0
    while True:
        code_exit.add(funcCMD('mosquitto_sub -t'+ name_topik))
        if i==0:
            print(code_exit[0]*0.6)
        if i==1:
            print(code_exit[1]*0.6+code_exit[0]*0.3)
        else:
            print(code_exit[i]*0.6+code_exit[i-1]*0.3+code_exit[i-2]*0.1)

pubTopik('Task4\data.txt', 'test/topik')
subTopik('test/topik')

