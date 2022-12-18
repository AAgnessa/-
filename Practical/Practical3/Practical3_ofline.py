import random
import math
class KNN:
    data=[]
    n=15
    proc =0.7

    def addData(self,data):
        self.data.append(data.copy())
    def setN(self,n):
        self.n=n

    def analyse(self, newData):
        distArr=[]
        for i in self.data:
            dist = ((i[0]-newData)**2)**0.5
            distArr.append([dist,i[1]])
        distArr.sort()
        #print (distArr)
        aCount,bCount=0,0
        for i in range(self.n):
            if distArr[i][1]=='a':
                aCount+=1
            else:
                bCount+=1
        #print (aCount/self.n,bCount/self.n,sep='\t')
        aCount=aCount/self.n
        bCount=bCount/self.n

        if aCount>=self.proc:
            return 'a'
        if bCount>=self.proc:
            return 'b'
        return "0"
    
    def printData(self):
        print(self.data)
        #for i in self.data:
            #print (i[0],i[1])

a=KNN()
buf=[0,0]
for i in range (2000):
    buf[0]=random.randint(0,100)
    buf[1]="a"
    a.addData(buf)
    buf[0]=random.randint(80,180)
    buf[1]="b"
    a.addData(buf)

for i in range (10):
    tmp=random.randint(0,180)
    #print (i, tmp,a.analyse(tmp))
