# pyPoll

# ------------------------- Instructions ------------------------------

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called election_data.csv.
# The dataset is composed of three columns: Voter ID, County, and Candidate.
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
 
# In addition, your final script should both:
#    print the analysis to the terminal and
#    and export a text file with the results.
# -----------------------------------------------------------------------------------------

# Import os and csv libraries
import os
import csv

# Assign filepath of read file to variable.
read_file_path = os.path.join('.', 'Resources', 'election_data.csv')

# Assign filepath of write (output) file to variable.
write_file_path = os.path.join('.', 'Analysis', 'election_analysis_output.txt')

# Create empty dictionary to track candidates and number of votes.
results = {}

# Open read file and return as file object.
with open(read_file_path, 'r') as read_file:

    # Return a reader object using comma delimiter
    rows = csv.reader(read_file, delimiter = ',')

    # Skip the header
    next(rows)

    # Loop through rows to count votes.
    for row in rows:
        
        # If candidate is not in the dictionary, add them as a key with a value of 1...
        if row[2] not in results.keys():
            results[row[2]] = 1
        
        # ... Otherwise, add 1 to the value for the candidate's key in the dictionary.
        else:
            results.update({row[2] : int(results[row[2]]) + 1})

# Sum the values (i.e., number of votes) in the dictionary.
total_votes = sum(results.values())
     
# Find key in dictionary with the largest value (i.e., the winning candidate).
winner = max(results, key = results.get)

# Create empty strings to save results as iterate through dictionary items.
results_text_output = ''
previous_text = ''

# Sort dictionary items by count of votes descending.
# Then loop through dictionary items to generate string with candidate, % of votes, and candidate votes.
# Each candidate prints on a different line.
for key, value in sorted(results.items(), key=lambda result: result[1], reverse=True):
    results_text_output = previous_text + (f'''{key}: {round(float(value) / float(total_votes) * 100, 2)}% ({value})
''')
    previous_text = results_text_output

# Variable to store the full text of the output.
full_text_output = (f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{results_text_output}-------------------------
Winner: {winner}
------------------------
''')

# Print results to the console.
print(full_text_output)

# Open write file and return as file object.
with open(write_file_path, 'w') as write_file:

     # Write results to the analysis (output) file.
    print(full_text_output, file = write_file)