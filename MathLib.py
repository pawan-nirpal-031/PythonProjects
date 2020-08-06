import math
import matplotlib.pyplot as plt

class GraphPlots:
    x=list()
    y =list()
    funs = list()

    def display(self,x,y):
        plt.plot(x,y)
        plt.show()

    def __init__(self):
        x =[]
        y =[]
        funs = ['sine','cosine','parabola','line']

    def FunValAt(self,fun,x,show): #under devlopment
        if(fun=='sine'):
            return GraphPlots().Sine(x,show)
        if(fun=='parabola'):
            return GraphPlots().Parabola(x[0],x[1],x[2],x[3],show)

    def Sine(self,r,d=False):
        self.x= [i for i in range(r+1)]
        self.y =[math.sin(i) for i in range(r+1)]
        if(d):
            self.display(self.x,self.y)
        return self.y[r]
    def NewObjct():
        return GraphPlots()
    def Cosine(self,r,d=False):
        self.x= [i for i in range(r)]
        self.y =[math.cos(i) for i in range(r)]
        if(d):
           self.display(self.x,self.y) 

    def Line(self,m,c,x,d =False):
        self.x = [i for i in range(x+1)]
        self.y = [m*i+c for i in range(x+1)]
        if(d):
           self.display(self.x,self.y) 
        return self.y[x]

    def Parabola(self,a,b,c,x,d=False):
        if((b**2-4*(a*c))>=0):
            self.x = [i for i in range(x+1)]
            self.y = [a*(i**2) + b*(i)+c for i in range(x+1)]
            if(d):
               self.display(self.x,self.y)
            return self.y[x]
        else:
            print('Invalid Graph make sure b^2 - 4ac>=0')


    

        
