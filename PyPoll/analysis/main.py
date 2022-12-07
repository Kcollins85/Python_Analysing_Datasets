#import the CSV file
import os
import csv

#create the path to the CSV
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#create the variables to tally the votes
total_votes = 0

#create the variables to track candidates, vote count & percentage
candidate = 0
candidate_list = []
candidate_tally = {}
winning_candidate = []
winning_tally = 0
winning_percent = 0
results_all =""

#open the file, specify the delimiter and set the variable parameters
with open(csvpath, 'r') as file:
    
    csvreader = csv.reader(file, delimiter=',')
    csvheader = next(csvreader)

    #start readying the file   
    for row in csvreader:
        #start tallying the votes
        total_votes += 1

        #create the list of candidates
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_tally[candidate] = 0
        candidate_tally[candidate] +=1

    #print the results to terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: "+ str(total_votes))
    print("-------------------------")
     
    #start the candidate alculations loop:
    for candidate in candidate_tally:
        #calculate the total number of votes each candidate won
        votes = candidate_tally[candidate]
        #calculate the percentage of votes each candidate won
        vote_percent = float(votes) / float(total_votes) * 100

        #print the results in terminal
        results = (f"{candidate}: {vote_percent:.3f}% ({votes})\n")
        print(results)

        #create the candidiate list results for the written file output
        results_all = results_all + results

        #find the winner of the election based on popular vote   
        if (votes > winning_tally):
            winning_tally = votes
            winning_candidate = candidate

    #print the winning candidate to terminal
    print("-------------------------")
    print("Winner: " +str(winning_candidate))
    print("-------------------------")

#creating a text file with the results
#Specify the path and file to write to
    output_path = os.path.join("..", "analysis", "election_results.txt")

#Open the file using "write" mode. Write the file with the election results
    with open(output_path, 'w') as csvfile:
        csvfile.write(f"Election Results: \n"
            f"-------------------------\n"
            f"Total votes: {total_votes}\n"
            f"-------------------------\n"
            f"{results_all}\n"
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            )