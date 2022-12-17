import git
#Задание 1
def simpleGeneratorFun():
    yield 3
    yield 2
    yield 1

for k in simpleGeneratorFun():
    print(k)

#Задание 2
#Класс для работы с файлами
class File:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print(f'Opening the file {self.filename}.')
        self.__file = open(self.filename, 'r')
        return self.__file
    def __exit__(self):
        print(f'Closing the file {self.filename}.')
        if not self.__file.closed:
            self.__file.close()
        return False
    def __write__(self):
        file = open(self.filename, "w")
        file.write(self.filename, 'FAIL')
        return file


a=File("Practical\\data.txt")
k=a.__enter__()
print(k.read())
#Функция для записи данных репозитория в файл
b=File("Practical\\data1.txt")
def copyRepo(gitUrl, repoDirectory):
    git.Repo.clone_from(gitUrl,repoDirectory)
    b.__write__()


