from os import replace
import matplotlib.pyplot as plt
import csv



unemp_rate = []
stck_indx_price = []
# n = int(input('Enter number of data points'))
# print('Enter unemployemnt data')
# for i in range(n):
#     e = int(input())
#     unemp_rate.append(e)

# print('Enter stock price data')
# for i in range(n):
#     e = int(input())
#     stck_indx_price.append(e)



def ScatterPlot(unemp_rate,stck_indx_price,plottype=1):
    if(plottype==1):
        plt.scatter(unemp_rate,stck_indx_price,color='red')
    else:
        plt.plot(unemp_rate,stck_indx_price,color='red')
    plt.title('Unemployemnt rate Vs Stock Index Price',fontsize = 14)
    plt.xlabel('Unemployemnt rate',fontsize = 14)
    plt.ylabel('Stock Index Price ',fontsize = 14)
    plt.grid(True)
    plt.show()


# pltTy = int(input('Enter plot type 1 for scatter 2 for line'))
# ScatterPlot(unemp_rate,stck_indx_price,pltTy)

country = ['usa','canada','germany','uk','france']
gdppc = [45000,42000,52000,49000,47000]

data = [unemp_rate,stck_indx_price,country,gdppc]

with open('data1.csv','w') as dataFile:
    write= csv.writer(dataFile)
    write.writerows(data)

def barChrt(country,gdppc):
    x = [i+0.5 for i,j in enumerate(country)]
    plt.bar(x,gdppc,color='teal')
    plt.title('Country vs GDP_Per_Cpaita',fontsize=14)
    plt.xlabel('Country',fontsize=14)
    plt.ylabel('GDP Per Capita',fontsize=14)
    plt.xticks(x,country)
    plt.show()

barChrt(country,gdppc)

