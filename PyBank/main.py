## import modules
import os
import csv

## Create lists to store the data
PLDelta = []
delta = 0
Date = []
PL = []
MyList = []
last_row_PL = 0
new_row_PL = 0
count_of_deltas = 0
total_months = 0
firstrow = True
total_delta = 0

## read csv file
finance_csv = os.path.join('.', 'Resources', 'budget_data.csv')

##open csv file
with open(finance_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #since there is a header row, skip reading the first row into the lists
    csv_header = next(csvreader)
    #initialize the net total of Profit and Losses variable
    netTotal = 0
    # Loop through reading the file and building lists to hold the data
    for row in csvreader:
        #Date.append(row[0])
        #PL.append(int(row[1]))
        #increment the counter for the total number of months
        total_months += 1
        netTotal += int(row[1])
        #calculate the changes in PL
        #skip the first DATA row calculation since it would skew the average, but do store the last_row_PL
        if firstrow:
            last_row_PL = int(row[1])
            firstrow = False
        else:
            #store what is now the previous row's P&L for purposes of calculation
            last_row_PL = new_row_PL
        # I have exited the if statement
        #assign the current row's P&L to variable
        new_row_PL=int(row[1])
        #calculate the change in P&L
        delta = new_row_PL - last_row_PL
        #Append to list with Date, Delta
        Date.append(row[0])
        PLDelta.append(delta)
        #update the total_delta
        total_delta += delta
        
        
        
        

## Calculations
#* The total number of months included in the dataset
print("------------------")
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total P&L: ${netTotal}")

 # * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
AvgDeltaPL = total_delta/(len(PLDelta)-1)
#print(f"Total Delta: +{total_delta}")
AvgDeltaPL = round(AvgDeltaPL,2)
print(f"Average Change: ${AvgDeltaPL}")


 # * The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(PLDelta)

print(f"Greatest increase in profits: {greatest_increase}")
#* The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(PLDelta)
print(f"Greatest decrease in losses: {greatest_decrease}")
print("------------------")

## write to txt in analysis folder
# Specify the file to write to
output_path = os.path.join(".", "Analysis", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
#text_file = open(output_path, 'w') #as csvfile:
with open(output_path,'w') as file_object:
    print("------------------",file=file_object)
    print("Financial Analysis",file=file_object)
    print("------------------",file=file_object)
    print(f"Total Months: {total_months}",file=file_object)
    print(f"Net Total P&L: ${netTotal}",file=file_object)
    print(f"Average Change: ${AvgDeltaPL}",file=file_object)
    print(f"Greatest increase in profits: {greatest_increase}",file=file_object)
    print(f"Greatest decrease in losses: {greatest_decrease}",file=file_object)
    print("------------------",file=file_object)