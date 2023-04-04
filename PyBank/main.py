import os
import csv

#variables for financial data set 

months = 0

row = 0

total_months = []

total_net = 0

net_change_list = []

greatest_increase = ["", 0]

greatest_decrease = ["", 9999999999999999999]
   
#import and read the budget data csv file; convert to dictionary based on "," spacing

with open("Resources/budget_data.csv", 'r') as financial_data:
    csvreader = csv.reader(financial_data, delimiter= ",")
    
#label header    
    header = next(csvreader)

#skip the header row     
    firstrow = next(csvreader)
    months += 1 
    total_net += int(firstrow[1])
    prev_net = int(firstrow[1])

#loop through each row and count each row for total months
    for row in csvreader:
    
        months += 1
        total_net += int(row[1])
#loop through each row and keep track of net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        total_months += [row[0]]
#calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
#calcualte greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#outside for loop calcualte net average 
    net_average = sum(net_change_list)/(len(net_change_list)-1)
#print solutions
print("Financial Analysis\n")

print("--------------------------------\n")

print(f"Total Months: {months}\n")

print(f"Total: {total_net}\n")

print(f"Average Change: {net_average}\n")

print(f"Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})\n")


print(f"Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})\n")

#export budget analysis data to text file
with open("Analysis/budget_data.txt", 'w') as financial_data:

    financial_data.write("Financial Analysis\n")

    financial_data.write("--------------------------------\n")

    financial_data.write(f"Total Months: {months}\n")

    financial_data.write(f"Total: {total_net}\n")

    financial_data.write(f"Average Change: {net_average}\n")

    financial_data.write(f"Greatest Increase in Profits: {greatest_increase[0]} ({greatest_increase[1]})\n")

    financial_data.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} ({greatest_decrease[1]})\n")