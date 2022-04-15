import os
import csv

ospath = 'C:\\Users\\wallh\\OneDrive\\Documents\\GitHub\\mattdhill011\\python-challenge\\PyPoll'
csvpath = os.path.join(ospath, 'Resources', 'election_data.csv')
output_path = os.path.join(ospath, 'analysis', 'analysis.txt')

# Open election_data.csv as election_data
with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    csv_header = next(election_data)
    # First we make an empty dictionary to contain all the canidate's names and their vote totals, as well as a variable to keep track of total votes
    canidates = {}
    total_votes = 0

    # Then loop through election_data 
    for entry in election_data:
        # Keep running tally of the total votes
        total_votes += 1

        # If we don't already have the canidate's name, we add them to the dictionary as a key and give them a single vote as the corresponding value
        if entry[2] not in canidates:
            canidates[entry[2]] = 1
        
        # If the are alread in the dictionary then we simply add a vote to their total
        else:
            canidates[entry[2]] += 1


# Now we output our data to a csv file
with open(output_path, 'w') as output:
    # We make a list containing an empty string and a number, as we loop through the canidates we will put in the canidate and vote count, replacing them if we find someone who has more votes
    winner = ["", 0]
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-------------------------\n")

    # Now we loop through the entries in the canidates dicionary
    for canidate in canidates:

        # First finding the percentage of votes that they have, rounded to 3 places and outputting their name, vote percentage and total votes
        percentage = round(((canidates[canidate] / total_votes) * 100), 3)
        output.write(f"{canidate}: {percentage}% ({canidates[canidate]})\n")

        # Now we check if the canidate has more votes than the current winner, if they do then we put their name and their vote count in the winner list
        if canidates[canidate] > winner[1]:
           winner[0] = canidate
           winner[1] = canidates[canidate]

    output.write("-------------------------\n")

    # Finally output the winner's name
    output.write(f"Winner: {winner[0]}\n")
    output.write("-------------------------\n")

# Now we print the output file to the terminal, stripping the new line characters
with open(output_path) as output:
    for line in output:
        print(line.strip())