#import the CSV file
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#create the variables
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_months = 0
total_net = 0
netchange_list = []
month_change = []

#open the CSV file
with open(csvpath, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    csvheader = next(csvreader)
    firstrow = next(csvreader)
    total_months =+ 1
    total_net =+ int(firstrow[1])
    prev_net = int(firstrow[1])
    
    #track the total net and months:
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])

        #track the net change and calculate the average:
        prev_net = int(firstrow[1])
        netchange = int(firstrow[1]) - prev_net
        netchange_list += [netchange]
        monthly_avg = sum(netchange_list) / len(netchange_list)

        # The greatest increase in profits (date and amount) over the entire period
        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange

        # The greatest decrease in profits (date and amount) over the entire period
        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange     



#printing the data in terminal
    print(" ")
    print("Financial Analysis: ")
    print("-------------------------")
    print("Total Months: " + str(total_months)) 
    print("Total profit/loss: " + str(total_net))
    print("Average change: "+ str(monthly_avg))
    print("Greatest Increase in Profits: " + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(greatest_decrease))

#creating a text file with the results
# Specify the file to write to
output_path = os.path.join("..", "analysis", "results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialise csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the rows:
    csvwriter.writerow("Financial Analysis: ")
    csvwriter.writerow("-------------------------")
    csvwriter.writerow("Total Months: " + str(total_months)) 
    csvwriter.writerow("Total profit/loss: " + str(total_net))
    csvwriter.writerow("Average change: "+ str(monthly_avg))
    csvwriter.writerow("Greatest Increase in Profits: " + str(greatest_increase))
    csvwriter.writerow("Greatest Decrease in Profits: " + str(greatest_decrease))