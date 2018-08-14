import os
import csv

def total_row_count():
    #Get the total number of rows (acctg periods in the file)
    global periods
    periods = len(list(csvreader))
    

def total_profit_calc():
    global total_profit

    for row in csvreader:
        total_profit += float(row[1])


# Path to collect data from the Budget_data csv file
budget_csv = os.path.join('..', 'budget_data.csv')

#Initialize variables

total_profit = 0

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Get the total Profits/Losses
    total_profit_calc()
   
    #Get the total row count
    periods = 0
    total_row_count()
      
    print("Total Months: " + str(periods))
    print(" ")

    formatted_profit = '${:,.2f}'.format(total_profit)
    print("Total: " + formatted_profit)
    



    





