#import the CSV file
import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#create the variables
total_votes = 0
candidate_list = 0
candidate_tally = []
percent_change = []
winner_tally = []

#open the CSV file
with open(csvpath, 'r') as file:
    
    # specift the delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')
    csvheader = next(csvreader)
    firstrow = next(csvreader)
    total_votes =+ 1
    
    # previousrow = (firstrow[1])
    # print(f"csv_header: {csv_header}")
       
    for row in csvreader:
        total_votes += 1
        sum = len(total_votes)
        print(sum)  

               
    #     #count the number of votes cast
    # sum = 0
    # rowcount = 0
    # for row in csvreader:
    #     rowcount += 1
    #     print(rowcount) 

#complete the list of candidates who recieved votes 

        # candidiate = row[2]
        # if firstrow != previousrow:
        #     sum = rowcount
        #     print(rowcount)

#create a dictionairy{
# percent
# sum
# }
#print(f'{candidiate["name"][]} " " {candidate[percent][]} " " {candidate[sum][]}')


# scroll through list and bring back when value changes
#when value changes, count the total number of rows
#calculate the percentage of these rows against the total votes count

    # the percentage of votes each candidate won
    # the total number of votes each candidate won
    # the winner of the election based on popular vote


#printing the data in terminal


    # print("Election results: ")
    # print("-------------------------")
    # print("Total votes: " + str(rowcount)) 
    # print("List of Candidates :")
    # print("Winner: ")

#creating a text file with the results
# Specify the file to write to
# output_path = os.path.join("..", "analysis", "election_results.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as csvfile:

#     # Initialise csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the rows:
#     csvwriter.writerow("Election results: ")
#     csvwriter.writerow("-------------------------")
#     csvwriter.writerow("Total votes: " + str(rowcount)) 
#     csvwriter.writerow("Total profit/loss: " + str(total_net))
#     csvwriter.writerow("List of Candidates :")
#     csvwriter.writerow("Winner: ")
