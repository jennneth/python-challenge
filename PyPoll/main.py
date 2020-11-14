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
winner_count = 0 #calculate the largest vote count
winner_name = "" #store the name of the candidate with the highest vote count
line_break = "--------------------" #stored as a variable for ease of reuse
print_list = [] #list of items to print to text file

# Specify the file to write to
output_path = os.path.join(".", "Analysis", "analysis.txt")

#this function whittles down the list of candidates to unique candidates
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
        
    #condense the list of candidates to a unique list of candidates
    unique_candidates = get_unique(all_candidates)
    
    #print to terminal the header of the report
    print(line_break)
    print("Election Results")
    print(line_break)
    print_list.append("\n"+line_break)
    print_list.append("\nElection Results")
    print_list.append("\n"+line_break)
    
    #* The total number of votes counted
    print(f"Total Votes: {total_votes}")
    print_list.append("\n"+ "Total Votes: " +str(total_votes))
    print(line_break)
    print_list.append("\n"+line_break)
    
    #for each unique candidate 
    for name in unique_candidates:
        #initialize counters for this candidate
        vote_count = 0
        vote_perc = 0
        #loop through all of the data stored in all_candidates (remember we loaded each row so a name = 1 vote)
        for x in all_candidates:
            #if the name in all candidates matches the unique candidate name we are looking at
            if x == name:
                #increment the vote count
                vote_count += 1
                #exit the if statement
            #while we are still on this unique candidate name, calculate the percentage of votes    
            vote_perc = vote_count/total_votes*100
            
            if vote_count > winner_count:
                winner_count = vote_count
                winner_name = name
        vote_perc_format = "{:.3f}".format(vote_perc)
        print(f"Candidate: {name}     Percentage of Vote: {vote_perc_format}%     Vote Count: {vote_count}")
        print_list.append("\nCandidate: "+name+"     Percentage of Vote: "+str(vote_perc_format)+"%     Vote Count: "+str(vote_count))
    print(line_break)
    print_list.append("\n"+line_break)
    print(f"Winner: {winner_name} !!!!!")
    print_list.append("\nWinner: "+winner_name)
    print(line_break)
    print_list.append("\n"+line_break)



# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path,'w') as file_object:
        file_object.writelines(print_list)

    