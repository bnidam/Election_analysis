# Get the data we need
# 1. The total number of votes cast
# 2. A complete list of candiates who received votes
# 3. The percentage of votes for each candidate
# 4. The total number of votes for each candidate
# 5. The winner of the election (most votes)

# Add the dependencies
import os
import csv

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

 # Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)


    # Print the header row.
    headers = next(file_reader)
    print(headers)

