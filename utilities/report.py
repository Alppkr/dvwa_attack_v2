import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import statistics

class report():
    responseTimeDict = {
        }
    responseTimeDict['Brute Force'] = [[]]
    responseTimeDict['Command Injection'] = [[]]
    responseTimeDict['File Inclusion'] = [[]]
    responseTimeDict['File Upload'] = [[]]
    responseTimeDict['SQL Injection Basic'] = [[]]
    responseTimeDict['SQL Injection Blind'] = [[]]
    responseTimeDict['XSS DOM'] = [[]]
    responseTimeDict['XSS Reflect'] = [[]]
    responseTimeDict['XSS Stored'] = [[]]

    attackDict ={
        }
    attackDict['Brute Force'] = [0,0,[]]
    attackDict['Command Injection'] = [0,0,[]]
    attackDict['File Inclusion'] = [0,0,[]]
    attackDict['File Upload'] = [0,0,[]]
    attackDict['SQL Injection Basic'] = [0,0,[]]
    attackDict['SQL Injection Blind'] = [0,0,[]]
    attackDict['XSS DOM'] = [0,0,[]]
    attackDict['XSS Reflect'] = [0,0,[]]
    attackDict['XSS Stored'] = [0,0,[]]


    @classmethod
    def blockedAttacked(self,sender):
        report.attackDict[sender][1] = self.attackDict[sender][1]+1


    @classmethod
    def successfulAttacked(self,sender,event):
        report.attackDict[sender][0] = self.attackDict[sender][0]+1
        report.attackDict[sender][2].append(event)
    

    @classmethod
    def response(self,sender,event):
        report.responseTimeDict[sender][0].append(event)


    def createImages(self):
        base_path = os.path.dirname(__file__)
        for i in self.attackDict:
            y = np.array([self.attackDict[i][0],self.attackDict[i][1]])
            plt.pie(y,labels=["Successful "+str(self.attackDict[i][0]),"Blocked "+str(self.attackDict[i][1])])
            plt.savefig(base_path+"/../outputs/"+i+"pie.png",format="png")
            plt.close()


    def printUnblockedAttacks(self):
        base_path = os.path.dirname(__file__)
        for i in self.attackDict:
            file_path = base_path+"/../outputs/"+i+".txt"
            with open(file_path,mode='w',encoding="ISO-8859-1") as f:
                for item in self.attackDict[i][2]:
                    f.write("%s\n" % item)
            f.close()

    
    def responseMeanTime(self):
        base_path = os.path.dirname(__file__)
        file_path = base_path+"/../outputs/responses.txt"
        with open(file_path,mode='w',encoding="ISO-8859-1") as f:
            for response in self.responseTimeDict:
                f.write(str(statistics.fmean(self.responseTimeDict[response][0]))+"\n")
            f.close()

    @classmethod
    def printAll(self):
        self.createImages(self)
        self.printUnblockedAttacks(self)
        self.responseMeanTime(self)