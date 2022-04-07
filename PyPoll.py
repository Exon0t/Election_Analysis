#Grab the Data from the ellection_results.csv
import csv
import os

totalvotes = 0
candidates = [ ]
candidatevotes = { }
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
        if row[2] not in candidates :
                candidates.append(row[2]) 
                print(candidates)

print(totalvotes)

#Write down the names of each candidate

#Get the total Votes for each candidate

#Get the total votes cast for the election