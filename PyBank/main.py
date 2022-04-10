import os
import csv


ospath = 'C:\\Users\\wallh\\OneDrive\\Documents\\GitHub\\mattdhill011\\python-challenge\\PyBank'
csvpath = os.path.join(ospath, 'Resources', 'budget_data.csv')
output_path = os.path.join(ospath, 'analysis', 'analysis.txt')

print("Financial Analysis")
print("----------------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    total_months = 0
    
    increase = 0
    decrease = 0


    for row in csvreader:
        profitLoss = float(row[1])
        total_months += 1
        total += profitLoss
        if profitLoss > increase:
            increase = profitLoss
        elif profitLoss < decrease:
            decrease = profitLoss
        
average_change = round(total / total_months, 2) 

with open(output_path, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("----------------------\n")
    output.write("Total Months: " + str(total_months) + '\n')
    output.write("Total: $" + str(total) + '\n')
    output.write("Average Change: $" + str(average_change) + '\n')
    output.write("Greatest Increase in Profits: " + str(increase) + '\n')
    output.write("Greatest Decrease in Profits: " + str(decrease) + '\n')

#now print from the output
with open(output_path) as output:
    for line in output:
        print(line.strip())
