'''
name : Pawan Nirpal
roll : TECOC341

'''

import numpy as np

class student:
    st_name =''
    st_class=''
    st_prn =''
    curr_sem =0
    mks_record = []

    def __init__(self,nm,clss,prn,sem):
        self.curr_sem  = sem
        self.st_class = clss
        self.st_name =nm
        self.st_prn = prn
        self.mks_record =[]
        self.sems_total_mks = []
        self.sem_max_min = []
        self.overall_max_min = []
        self.over_all_aggre =0
        self.is_pass = True
    
    def get_marks(self):
        if(self.curr_sem==1):
            print('Student of sem 1 is not allowed ')
            return
        try:
            record =[]
            over_min =10000
            over_max = 0
            for i in range(1,self.curr_sem):
                print('Enter marks for 5 subjects for sem : '+str(i)+' : ')
                sub_mks =[]
                sem_sum=0
                sem_max = 0
                sem_min = 10000
                for sub in range(1,6):
                    x=int(input())
                    if x<40:
                        self.is_pass = False
                    sem_sum+=x
                    sub_mks.append(x)
                    over_min = min(over_min,x)
                    over_max = max(x,over_max)
                    sem_max = max(sem_max,x)
                    sem_min = min(sem_min,x)
                self.sems_total_mks.append(sem_sum)
                self.sem_max_min.append((sem_max,sem_min))
                record.append(sub_mks)
            self.over_all_aggre = np.sum(self.sems_total_mks)
            self.overall_max_min.append((over_max,over_min))
            self.mks_record = np.array(record)
        except Exception:
            print('Error occoured')
        
    def details(self):
        print(self.over_all_aggre)
        print('overall max,min marks')
        print(self.overall_max_min)
        try:
            print('overall percentage : '+str(float((self.over_all_aggre)/(500*(self.curr_sem-1)))*100))
        except ArithmeticError:
            print('Student of 1st sem is not allowed')


        
    def show_student_info(self):
        print('name : '+self.st_name)
        print('class : '+self.st_class)
        print('prn : '+self.st_prn)
        self.show_record()
        
        print('Sem wise aggregate ')
        print(self.sems_total_mks)

        if self.is_pass:
            print('Student passed with overall aggregate ')
            self.details()
        else:
            print('student failed')
            self.details()
        


    def show_record(self):
        for sem in range(1,self.curr_sem):
            print('Marks of '+str(sem)+' sem ')
            print(self.mks_record[sem-1])


print('Enter details for two students , note that student 1 sem is not a vaild entry')
data_base =[]

for s in range(1):
    nm = input('Enter student name  ')
    cl = input('Enter class FE/SE/TE/BE  ')
    prn = input('Enter student prn  ')
    curr_sem = int(input('Enter current sem number  '))
    if curr_sem!=1:
        stud = student(nm,cl,prn,curr_sem)
        stud.get_marks()
        data_base.append(stud)
    else:
        print('Sem 1 students not allowed')

for st in data_base:
    st.show_student_info()
    print('\n')

