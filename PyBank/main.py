#import data
import os
import csv

#Store data
Pybank_csv = 'budget_data.csv'
Date_ = 'Date'
Profit_Losses = 'Profit/Losses'

def calculate_total_months():
    # 1.1 Set the path for the file
    Pybank_csv = os.path.join( 'Resources', 'budget_data.csv')

    # 1.2 Read trough the csv
    month_count = 0
    with open (Pybank_csv, 'r') as csvfile:
        csv_reader = csv.reader(csvfile,delimiter = ',')

        # 1.2.1 Loop trough the file if line > 0 we will increase month_count in 1
        lines = 0
        for row in csv_reader:
            if lines > 0:
                month_count += 1
            lines += 1

    # 1.3 Return the result
    return month_count

def calculate_total_amount_profit_losses():
    # 2.1 Set the path for the file
    Pybank_csv = os.path.join( 'Resources', 'budget_data.csv')

    #2.2 Read trough the csv
    with open (Pybank_csv, 'r') as csvfile:
        csv_reader = csv.reader(csvfile,delimiter = ',')

        # 1.2.1 Loop trough the rows & calculate rows values by adding the previous value 
        lines = 0
        for row in csv_reader:
            if lines > 0:
                total_amount = total_amount + int(row[1])
            lines +=1

        #1.3 Return the result
        return total_amount

def calculate_average_changes():
    #3.1 Set the path for the file
    Pybank_csv = os.path.join( 'Resources', 'budget_data.csv')

    #3.2 Read trough the csv
    month_cont = 0
    total_amount = 0
    with open (Pybank_csv, mode = 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ',')

        # 3.2.1 
        #loop trough the file & 
        # Increasing the months counts and adding the previous values to the  row [1] (profit/losses)
        lines = 0
        for row in csv_reader:
            if lines > 0:
                month_cont = month_cont + 1
                total_amount = total_amount + int(row[1])
            lines +=1

        # 3.3 Return the result
        return total_amount/month_cont

   





