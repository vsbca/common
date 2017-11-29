import csv
from datetime import datetime

with open('cvedata.csv','rb') as f:
    f.next()
    reader = csv.reader(f, delimiter=',')
    for line in reader:
       #date1 is on column 2 and column 9
        date1 = line[1]
        date3 = line[8]
        #date is of format 12/09/2017
        date1=datetime.strptime(date1,"%d/%m/%Y").date()
        date3=datetime.strptime(date3,"%d/%m/%Y").date()

        delta=(date3 - date1).days
        print(delta)
        
