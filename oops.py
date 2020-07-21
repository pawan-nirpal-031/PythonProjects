class animal:
    age =0
    food ="none"
    def make_noise(self):
        print('bark')

an = animal()
an.make_noise()
print(dir(an))