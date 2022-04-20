#Grab the Data from the ellection_results.csv
import csv
import os

totalvotes = 0
candidates = [ ]
countys = [ ]
candidates_votes = { }
county_votes = { }
election_results = ""
county_results = ""
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
#outfile = open(file_to_save, "w")
#read and analyse the data here
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        next(file_reader)
#Grabs all Candidates names
        for row in file_reader:   
                totalvotes= totalvotes+ 1
                candidates_name = row[2]
                if candidates_name not in candidates :
                        candidates.append(candidates_name) 
                        candidates_votes[candidates_name]=0
#adds one to candidates votes
                candidates_votes[candidates_name] += 1
        winning_votes = 0
#gets all county names
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        next(file_reader)        
        for row in file_reader:
                county_name = row[1]
                if county_name not in countys:
                        countys.append(county_name)
                        county_votes[county_name]=0
#adds one to county's votes
                county_votes[county_name] += 1
winning_county_votes = 0 
# gets the percentage and highest county votes
for county_name in county_votes:
        votes= county_votes[county_name]
        county_percentage = votes / totalvotes *100
        county_results = county_results + f"{county_name} : {county_percentage:.1f}% ({votes:,})\n"
        if winning_county_votes < votes:
                winning_county = county_name
                winning_county_votes = votes
                winning_county_percentage = county_percentage



        



#gits percentage of votes using the total and the candidates votes
for candidates_name in candidates_votes:
        votes = candidates_votes[candidates_name]
        vote_percentage = (votes / totalvotes) * 100
        election_results = election_results + f"{candidates_name} : {vote_percentage:.1f}% ({votes:,})\n"
        #grabs winning names, percentage and votes
        if winning_votes < candidates_votes[candidates_name]:
                winning_votes = candidates_votes[candidates_name]
                winning_candidate = candidates_name
                winning_percentage = vote_percentage
#count county votes
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_votes:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
winning_county_summary = (
        f"-------------------------\n"
        f"Highest Votes County : {winning_county}\n"
        f"Highest Votes Count : {winning_county_votes:,}\n"
        f"Highest Votes Percentage : {winning_county_percentage:.1f}%\n"
        f"-------------------------\n"
)

election_results = (
        f"Election Results \n"
        f"----------------------\n"
        f"Total Votes: {totalvotes:,}\n" 
        f"----------------------\n"+
        election_results +
        f"----------------------\n"+
        county_results
)
print(election_results)
print(winning_candidate_summary)
print(winning_county_summary)
with open(file_to_save, "w") as text_file:
        text_file.write(election_results)
        text_file.write(winning_county_summary)
        text_file.write(winning_candidate_summary)
