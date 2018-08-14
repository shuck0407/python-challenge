import os
import csv
import operator 



profit_list = []
profit_period = []
change_list = []

def total_calcs():
    global total_profit
    global periods
    global first_number
    global last_number
    global avg_change
    global max_change
    
    rownum = 0
    old_profit = 0
   
    for row in csvreader:
        
       #Get the new profit number for use in change calculation
        new_profit = float(row[1])

        change_profit = new_profit - float(old_profit)

        acctg_period = str(row[0])

        profit_list.append(change_profit)
        profit_period.append(acctg_period)
        old_profit = new_profit

        #Accumulate the total profit
        total_profit += float(row[1])

        #Accumuate the number of periods in the file
        periods += 1

        #Get the first profit number to use in avg calculation
        if rownum == 0:
            first_number = float(row[1])
        rownum += 1  
            
    last_number = float(row[1])

    #Calculate the average change over the period

    avg_change = (last_number - first_number) / (periods - 1)

       
# Path to collect data from the Budget_data csv file
budget_csv = os.path.join('..', 'budget_data.csv')

#Initialize variables

total_profit = 0
periods = 0


# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Get the total Profits/Losses
    total_calcs()

    print("Total Months: " + str(periods))
    print(" ")

    formatted_profit = '${:,.2f}'.format(total_profit)
    print("Total: " + formatted_profit)
    
    formatted_average = '${:,.2f}'.format(avg_change)
    print("Average Change: " + formatted_average)

     #zip up the periods and changes
    change_list = list(zip(profit_period, profit_list))
    #print(change_list)

    max_profit_change = max(change_list, key=operator.itemgetter(1))
    min_profit_change = min(change_list, key=operator.itemgetter(1))

    formatted_max = '${:,.2f}'.format(max_profit_change[1])
    print("Greatest Increase in Profits: "+ max_profit_change[0] + " " + formatted_max)

    formatted_min = '${:,.2f}'.format(min_profit_change[1])
    print("Greatest Decrease in Profits: "+ min_profit_change[0] + " " + formatted_min)


    


  






    





