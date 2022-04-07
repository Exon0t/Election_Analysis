#Grab the Data from the ellection_results.csv
import csv
import os

totalvotes = 0
candidates = [ ]
candidates_votes = { }
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
#outfile = open(file_to_save, "w")
#read and analyse the data here
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        next(file_reader)
        for row in file_reader:   
                totalvotes= totalvotes+ 1
                candidates_name = row[2]
                if candidates_name not in candidates :
                        candidates.append(candidates_name) 
                        candidates_votes[candidates_name]=0

                candidates_votes[candidates_name] += 1
wining_votes = 0
for candidates_name in candidates_votes:
        votes = candidates_votes[candidates_name]
        vote_percentage = (votes / totalvotes) * 100
        print(f"{candidates_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if wining_votes < candidates_votes[candidates_name]:
                wining_votes = candidates_votes[candidates_name]
                wining_candidate = candidates_name
                wining_percentage = vote_percentage

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {wining_candidate}\n"
    f"Winning Vote Count: {wining_votes:,}\n"
    f"Winning Percentage: {wining_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#Write down the names of each candidate

#Get the total Votes for each candidate

#Get the total votes cast for the election