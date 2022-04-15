
import os
import csv


ospath = 'C:\\Users\\wallh\\OneDrive\\Documents\\GitHub\\mattdhill011\\python-challenge\\PyBank'
csvpath = os.path.join(ospath, 'Resources', 'budget_data.csv')
output_path = os.path.join(ospath, 'analysis', 'analysis.txt')
# Open budget_data.csv as budget_data
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_data)

    # Now we set our variables, starting with total and total months set to 0
    total = 0
    total_months = 0

    # The plan is to loop through the rows of the csv file and at the end of the loop set this variable to the current month's profits so we can carry it over to the next loop
    last_month_profitLoss = 0

    # For greatest increase and greatest decrease we want to store 2 pieces of data, the date and the change in profits, so I make a list with two elements, a string and a float.
    # We are just going to set the list elements to equal what we want, but I like setting it up this way so I can remember which index is supposed to be the string and which is the float.
    increase = ['', 0.0]
    decrease = ['', 0.0]

    # Now loop throught the data
    for row in budget_data:
        # Grab the value in the second column and set it equal to profitLoss
        profitLoss = float(row[1])

        # Keep count of how many months
        total_months += 1

        # Keep a running tally of the total profits and losses
        total += profitLoss

        # We want difference in the profits from this month and the last month. So we subtract last month's profitLoss from this month's.
        profit_change = profitLoss - last_month_profitLoss

        # Now we check if the change in profits is higher than the highest increase we've seen so far or lower than the lowest decrease and set the the two elements of the list to profit_change and data
        if profit_change > increase[1]:
            increase[1] = profit_change
            increase[0] = row[0]

        elif profit_change < decrease[1]:
            decrease[1] = profit_change
            decrease[0] = row[0]
        
        # Now we carry over the profitLoss to the next loop
        last_month_profitLoss = profitLoss

# We find the average change by just taking the total and divide by the total number of months. Also round it to 2 places since fractions of cents don't make sense       
average_change = round(total / total_months, 2)


with open(output_path, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("----------------------\n")
    output.write("Total Months: " + str(total_months) + '\n')
    output.write("Total: $" + str(total) + '\n')
    output.write("Average Change: $" + str(average_change) + '\n')
    output.write(f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n")
    output.write(f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n")

# Now print from the output to the terminal
with open(output_path) as output:
    for line in output:
        print(line.strip())