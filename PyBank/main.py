#import data
import os
import csv

#Set the path for the file
Pybank_csv = os.path.join( 'Resources', 'budget_data.csv')

#open the csv
with open (Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    for row in csvreader:
        #profit.append(row[1])
        print(f"Profit: {sum(row[1])}")
 #create header row
    #csv_header = next(csvreader)
    print("Financial Data")
    print("-----------------------------") 
    
#total number of months included in the dataset
    months = len(list(csvreader))
    print("Total number of months:" + str(months) )

#read the rows after the header
   # date = []
   # profit = []



#print(f'Total Profit: {sum(profit)}')
