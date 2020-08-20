class Employee:
    id=0
    name = ""
    def __init__(self):
        self.id =0;
        self.name = ""
    def __init__(self,i,n):
        self.id = i
        self.name = n
    def show(self):
        print(str(self.id)," : ",self.name)
    def walk(self,x,y):
        print(self.name + " walking : "+str(x)+" ; "+str(y))

e1 = Employee(1,"homer")
e1.walk(1,2)
e1.show()