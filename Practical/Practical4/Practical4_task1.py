#Задание 1
def simpleGeneratorFun(count):
    for i in range(count):
        if i%2==0:
            yield i


for k in simpleGeneratorFun(10):
    print(k)