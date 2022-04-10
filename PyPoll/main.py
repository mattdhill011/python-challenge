import os
import csv

ospath = 'C:\\Users\\wallh\\OneDrive\\Documents\\GitHub\\mattdhill011\\python-challenge\\PyPoll'
election_csv = os.path.join(ospath, 'Resources', 'election_data.csv')
output_path = os.path.join(ospath, 'analysis', 'analysis.txt')

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #first we make an empty dictionary to contain all the canidate's names and their vote totals
    canidates = {}
    total_votes = 0


    for entry in csvreader:
        #keep running tally of the total votes
        total_votes += 1

        #if we don't already have the canidate's name, we add them to the list and give them a single vote
        if entry[2] not in canidates:

            #we're making the entry a list containing 2 numbers, we will use the second one to enter the percent votes at the end
            canidates[entry[2]] = 1
        
        #otherwise we add a vote to the canidates tally
        else:
            canidates[entry[2]] += 1


#now we output our data
with open(output_path, 'w') as output:
    #We make a list containing an empty string and a number, as we loop through the canidates we will put in the canidate and vote count, replacing them if we find someone who has more votes
    winner = ["", 0]
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-------------------------\n")
    for canidate in canidates:
        percentage = round(((canidates[canidate] / total_votes) * 100), 3)

        output.write(f"{canidate}: {percentage}% ({canidates[canidate]})\n")
        if canidates[canidate] > winner[1]:
           winner[0] = canidate
           winner[1] = canidates[canidate]

    output.write("-------------------------\n")
    output.write(f"Winner: {winner[0]}\n")
    output.write("-------------------------\n")

#now we print the file to the terminal
with open(output_path) as output:
    for line in output:
        print(line.strip())



    





