#import the CSV file
import os
import csv

#create the path to the CSV
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# create the variables to calculate the results
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["" , 0]
greatest_decrease = ["" , 9999999999999999999]
total_net = 0

#open the file and set the variable parameters
with open (csvpath) as file:
    reader = csv.reader(file)
    header = next(reader)
    firstrow = next(reader)
    total_months += 1
    total_net += int(firstrow[1])
    previousnet = int(firstrow[1])

    #start reading the file
    for row in reader:
        #track total months
        total_months += 1
        total_net += int(row[1])

        #track the net change
        netchange = int(row[1]) - previousnet
        previousnet = int(row[1])
        net_change_list += [netchange]

        #calculate the greatest increase       
        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange

        #calculate the greatest decrease
        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange

#calculate the average
monthly_average = sum(net_change_list) / len(net_change_list)

#consolidate the results
output = (f"Financial Analysis: \n"
        f"----------------------\n"
        f"Total Months:  {total_months}\n"
        f"Total profit/loss: ${total_net}\n"
        f"Average Change: ${monthly_average:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase}\n"
        f"Greatest Decrease in Profits: {greatest_decrease}\n")

#print the results in terminal
print(output)

#creating a text file to print the results
#specify the file to write to
output_path = os.path.join("..", "analysis", "financial_analysis_results.txt")

#open the file using "write" mode. Specify the variable details to write to the file
with open(output_path, 'w') as csvfile:
    csvfile.write(output)