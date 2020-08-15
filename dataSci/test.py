import csv
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

def AvgCityFuel(data):
    sum =0
    for d in data:
        sum+=(float(d['mpg']))
    return (float(sum/len(data)))

def UniqueCylinderValues(data):
    cylinders = set(d['cylinders'] for d in data) 
    return (cylinders)

def MpgByCylinderTypes(data):
    MpgCyls=list()
    uniqueCyls = UniqueCylinderValues(data)
    for cy in uniqueCyls:
        cnt =0
        sumd =0
        for tbl in data:
            if(tbl['cylinders']==cy):
                sumd+=float(tbl['cylinders'])
                cnt+=1
        MpgCyls.append((cy,(sumd/cnt)))
    return MpgCyls

#print(MpgByCylinderTypes(mpg))
x = range(1000)
print(type(x))