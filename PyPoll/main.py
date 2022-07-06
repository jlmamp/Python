 # import the csv and as modules
import csv
import os

from sympy import N
# load the file to read the survey data
inputFile = os.path.join("resources", "election_data.csv")

# output file location for election analysis
outputfile = os.path.join("Analysis folder","electionanalysis.txt")

# variables
totalVotes = 0 # variable that holds the total number of votes
candidates = []   # list of candidates that recevied votes
candidatesVotes = {} # dictionary that hold total votes for each candidate
WinningCount = 0 # Winning count is held within this varible 
winningCandidate = "" # varible for winning candidate 


# read the csv file
with open(inputFile) as electionData:
    #create the csv reader
    csvreader = csv.reader(electionData)
    # read the header
    header = next(csvreader)
    #row will be lists
        # index 0 is the Ballot ID
        # index 1 is the country

    # for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1 # same as totalVotes = totalVotes + 1

    # check to see if the candidates are in the list
        if row[2] not in  candidates:
            candidates.append(row[2])

        # add vlaue to dictionary
        # {"key": vlaue}
        # start the count at 1 for the votes
            candidatesVotes[row[2]] = 1


        else:
        # the candidate is in the list 
        # add a vote to the candidate's count 
            candidatesVotes[row[2]] += 1

# print(candidatesVotes)
voteOutput = ""



for candidate in candidatesVotes:
    # get percent/vote count of the votes
    votes = candidatesVotes.get(candidate)
    votePct = (float(votes) / float(totalVotes)) * 100.00

    voteOutput += f"{candidate}: {votePct:.3f}% ({votes:,})\n"

    # compare the votes to the winning count
    if votes > WinningCount:
        # update the votes to be the new win count
        WinningCount = votes
        # update the winning candidate 
        winningCandidate = candidate


winningCandidateOutput = f"WINNER: {winningCandidate}\n-------------------------------------"

# create as output variable to hold the output
output = (
    f"\n\nElection Data Results\n"
    f"-------------------------------------\n"
    f"Total Votes: {totalVotes:,}\n-------------------------------------"
    f"\n{voteOutput}-------------------------------------"
    f"\n{winningCandidateOutput}"
)

# display output to the console
print(output)

# Exports results to electionanalysis.txt
with open(outputfile, "w") as textFile:
    # output to the text file
    textFile.write(output)




