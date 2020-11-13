#copied code from PyBank, will modify
#PyPoll program
#*************   Assignment:    ***********************
#  In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#  * The total number of votes cast

# * A complete list of candidates who received votes

#  * The percentage of votes each candidate won

#  * The total number of votes each candidate won

#  * The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:

#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#************ PROGRAM STARTS***********************
## import modules
import os
import csv

## Create and initialize variables
total_votes = 0 #total votes cast
all_candidates= []  #list of all candidates
unique_candidates = [] #list of unique candidates
khan_votes = 0 #number of votes for Khan
correy_votes = 0 #number of votes for correy
li_votes = 0 #number of votes for Li
otool_votes = 0 #number of votes for O'Tooley
khan_perc = 0 #percentage of votes for Khan
correy_perc = 0 #percentage of votes for correy
li_perc = 0 #perc of votes for Li
otool_perc = 0 #percentage of votes for O'Tooley

#this module whittles down the list of candidates to unique candidates
def get_unique(candidates):
    unique = []
    for candidate in candidates:
        if candidate not in unique:
            unique.append(candidate)
    return unique

## read csv file
vote_csv = os.path.join('.', 'Resources', 'election_data.csv')

##open csv file
with open(vote_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #since there is a header row, skip reading the first row into the lists
    csv_header = next(csvreader)
    # Loop through reading the file and take appropriate action
    for row in csvreader:
        #increment the counter for the total number of votes
        total_votes += 1
        #add the candidate to the all candidate list
        all_candidates.append(row[2])
        #count who the vote is for
        if row[2] = "Khan":
            khan_votes += 1
        elif row[2] = "Correy":
            correy_votes += 1
        elif row[2] = "Li":
            li_votes += 1
        elif row[2] = "O'Tooley":
            otool_votes += 1
        #end of if statement
         
    unique_candidates = get_unique(all_candidates)
    print(f"List of all candidates: {unique_candidates}")
        
  
## Calculations & Printouts

print("------------------")
print("Election Results")
print("------------------")
#* The total number of months included in the dataset
print(f"Total Votes: {total_votes}")
print("------------------")

#* Votes percentage and raw count per candidate
#calculate & format percentage votes for each candidate
khan_perc = round((khan_votes/total_votes)*100,3)
correy_perc = round((correy_votes/total_votes)*100,3)
li_perc = round((li_votes/total_votes)*100,3)
otool_perc = round((otool_votes/total_votes)*100,3)
print(f"Khan: {khan_perc} (khan_votes}")
print(f"Correy: {correy_perc} {correy_votes}")
print(f"Li: {li_perc} {li_votes}")
print(f"O'Toole: {otool_perc} {otool_votes}")

 # * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#AvgDeltaPL = total_delta/(len(PLDelta)-1)
AvgDeltaPL = sum(PLDelta)/(len(PLDelta)-1)
#format the AvgDeltaPL to 2 decimal places
AvgDeltaPL = round(AvgDeltaPL,2)
print(f"Average Change: ${AvgDeltaPL}")


 # * The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(PLDelta)

print(f"Greatest increase in profits: {date_largest} ${greatest_increase}")
#print(f"Greatest increase in profits2: {delta_largest}")
#print(f"Greatest increase date: {date_largest}")
#* The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(PLDelta)
print(f"Greatest decrease in losses: {date_smallest} ${greatest_decrease}")
#print(f"Greatest decrease in profits2: {delta_smallest}")
#print(f"Greatest decrease date: {date_smallest}")
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
    print(f"Greatest increase in profits: {date_largest} ${greatest_increase}",file=file_object)
    print(f"Greatest decrease in losses: {date_smallest} ${greatest_decrease}",file=file_object)
    print("------------------",file=file_object)