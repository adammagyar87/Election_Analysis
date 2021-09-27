# Election Analysis

## Project Overview
An employee from the Colorado Board of Elections asked me to audit a local congressional election via Python. The script written for this audit was then be applied to other elections where the data is stored in the same format. The application will display the data in the terminal as well as write them to a text file. The information requested is as follows:

1. Calculate the total number of votes cast. 
2. Compile a complete list of candidates which received votes.
3. Find the total number of votes for each candidate.
4. Find the vote percentage for each candidate.
5. Determine the election winner via popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.2, Visual Studio Code 1.60.2 

## Election Audit Results
The election audit results demonstrate:

- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The votes and percentages were:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
  - Diana DeGette: 73.8% (272,892)

## Election Audit Summary

Screen grab of the terminal seen below:

![image](https://user-images.githubusercontent.com/87042597/134835370-a6091a71-8eb1-4dac-aff3-40aa6aa40408.png)

The results are also printed to the election_results.txt file in the "analysis" folder. This script can be re-utilized for other elections with minor changes. The filepath and filenames after "file_to_load" and "file_to_save" will need to be customized for each specific case. The specific section of the code is in lines 4 - 7 seen below:

```
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```

Other changes that may be needed for clarity would be the names of the variables. This code was written with this specific election in mind. If this were a city wide election, the use of "counties" in the code could cause confusion. 

Another similar example would be the variables where specific wording is held and printed to the terminal and the output text file. An example from lines 80 - 92 is seen below:

```
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
  ```
  
 This wording would not work in different types of elections.
