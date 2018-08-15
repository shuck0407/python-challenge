import os
import csv


#Get the file path

election_csv = os.path.join('..', 'Small_Election_Data.csv')

#Injest the csv file into a dictionary

with open(election_csv, 'r') as csvfile:  
    reader = csv.DictReader(csvfile)

    for row in reader:
        for key, value in row.items():
            print(value[1])
    
    
    