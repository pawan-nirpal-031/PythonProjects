import math
import matplotlib.pyplot as plt

class graph:
    x=list()
    y =list()
    def __init__(self):
        x =[]
        y =[]
    def getFunVal(self,x):
        return self.y[x]
    def sinGraph(self,r):
        self.x= [i for i in range(r)]
        self.y =[math.sin(i) for i in range(r)]
        plt.plot(self.x,self.y)
        plt.show()
    def cosGraph(self,r):
        self.x= [i for i in range(r)]
        self.y =[math.cos(i) for i in range(r)]
        plt.plot(self.x,self.y)
        plt.show()
    def lineGraph(self,m,c):
        self.x = [i for i in range(1000)]
        self.y = [m*i+c for i in range(1000)]
        plt.plot(self.x,self.y)
        plt.show()
    
    
g1 = graph()

        
