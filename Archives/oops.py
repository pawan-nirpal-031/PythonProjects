class animal:
    xpos =0
    ypos =0
    name =""
    def __init__(self,nm="none"):
        print('hello I am ',nm)
        self.name = nm
    def __del(self):
        print("time to say goodbye", self.name)
    def noise(self,n):
        print("z....",n)
    def move(self,x,y):
        self.xpos = x
        self.ypos = y
        print('walking happily ',self.xpos," , ",self.ypos)

class dog(animal):
    def __init__(self,ji):
        print("lets bark!",ji)
        animal.name = ji
    animal("dory").move(11,2)
    def myn(self):
        print('hello ',self.name)


a1 = animal("boog")
a2 = animal("sory")
a1.move(1,2)
a2.move(3,4)
a1.noise("bark")
a2.noise("doek")
dog('bog').myn()