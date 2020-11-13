## import modules
import os
import csv

## Create and initialize variables
PLDelta = []
delta = 0 #difference in two months PL
MyList = []
last_row_PL = 0 #data value of the previous row 
new_row_PL = 0 #data value of the current row
count_of_deltas = 0
total_months = 0 #initialize the variable to count the total months in the dataset
firstrow = True #determines if this is the first row of data, used in IF statement
total_delta = 0
netTotal = 0 #initialize the variable to count the total PL for all months
delta_largest = 0 #initialize variable to hold largest delta
delta_smallest = 0 #initialize variable  to hold the smallest delta
date_largest = 0 #initialize the variable to hold the month of the largest delta
date_smallest = 0 #initialize the variable to hold the month of the smallest delta

## read csv file
finance_csv = os.path.join('.', 'Resources', 'budget_data.csv')

##open csv file
with open(finance_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #since there is a header row, skip reading the first row into the lists
    csv_header = next(csvreader)
    # Loop through reading the file and building lists to hold the data
    for row in csvreader:
        #increment the counter for the total number of months
        total_months += 1
        #add each rows PL value to the netTotal counter
        netTotal += int(row[1])
        #calculate the changes in PL
        #skip the first DATA row PLdelta calculation since it would skew the average, and store the last row DATA in variable
        if firstrow:
            last_row_PL = int(row[1])
            firstrow = False
        else:
            #store what is now the previous row's P&L for purposes of calculation
            last_row_PL = new_row_PL
        # exit the IF statement
        #assign the current row's P&L to variable
        new_row_PL=int(row[1])
        #calculate the change in P&L
        delta = new_row_PL - last_row_PL
        #Add the delta calculation to the end of the list PLDelta
        PLDelta.append(delta)
        #If the delta is the biggest or the smallest, store that number and store the date.
        if delta > delta_largest:
            date_largest = row[0]
            delta_largest = delta
        elif delta < delta_smallest:
            date_smallest = row[0]
            delta_smallest = delta
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
print(f"Greatest increase in profits2: {delta_largest}")
print(f"Greatest increase date: {date_largest}")
#* The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(PLDelta)
print(f"Greatest decrease in losses: {greatest_decrease}")
print(f"Greatest decrease in profits2: {delta_smallest}")
print(f"Greatest decrease date: {date_smallest}")
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