# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

#Initialize list for all candidates
candidate_options = []

#Initiate empy dictionary for counting votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)
    
    #Print each row of csv
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Find the candidate name from each row
        candidate_name = row[2]
        #If the candidate's name does not already appear in the candidate_options list
        if candidate_name not in candidate_options:
            #Add it to candidate_options list
            candidate_options.append(candidate_name)
        
            #Begin tracking votes
            candidate_votes[candidate_name] = 0

        # Begin to tally candidates votes
        candidate_votes[candidate_name] += 1
        

#Total number of votes cast (removed via module instructions)
#print(total_votes)

#A complete list of candidates who received votes (removed via module instructions)
#print(candidate_options)

#Print the candidate vote dictionary (removed via module instructions)
#print(candidate_votes)


#Total number of votes each candidate received skipped this


#Percentage of votes each candidate won
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
#   To do: print out the winning candidate, vote count and percentage to terminal.       
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#The winner of the election based on popular vote
