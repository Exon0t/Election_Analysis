#Grab the Data from the ellection_results.csv
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
#read and analyse the data here
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     next(file_reader)
     for row in file_reader:
        print(row[0])
#Write down the names of each candidate
outfile.write("Hello World")
outfile.write("Denver\n")
outfile.write("Denver\n")
outfile.write("Denver\n")
outfile.write("Denver\n")

outfile.close()
#Get the total Votes for each candidate

#Get the total votes cast for the election