from git import Repo

#Функция для чтения имен репозиториев из файла
def funcForReadFile(name_fale):
    arrayWithNameRepo=[]
    try:
        file = open(name_fale, 'r')
    except:
        print("Sistem error, file not open")
    with file:
        lines = file.readlines()
        for line in lines:
            arrayWithNameRepo.append(line)
    
    return arrayWithNameRepo
# k=funcForReadFile("Practical\\Practical4\\data.txt")
# print(k)

def copyRepo(gitUrl: str, repoDirectory:str):
    try:
        Repo.clone_from(gitUrl,repoDirectory)
        #result=gitUrl+'OK'
    except:
        print('Error with copy repo')
        #result=gitUrl+'FAIL'
    #return result


#copyRepo('git@github.com:AAgnessa/NATS.git','NATS.git-ssh')
if __name__ == '__main__':
    Result=[]
    gits=funcForReadFile("Practical\\Practical4\\data.txt")
    for git in gits:

        git_Url = git.rstrip()
        if 'https://github.com' in git_Url:
            repo_Directory = git.rstrip().split('/')[-1] + '-https'
        elif 'git@github.com' in git_Url:
            repo_Directory = git.rstrip().split('/')[-1] + '-ssh'
        else:
            print('Error with URL git')
        copyRepo(git_Url,repo_Directory)
        #print(git_Url,repo_Directory)
        #Result.append(copyRepo(git_Url,repo_Directory))
    #print(Result)

