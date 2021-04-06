  
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')



Votes = []
Candidate_Votes = {}
Candidates = []
Winning_Votes = 0
Winning_Candidates = ""


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    print(csvreader)
    
    csv_header = next(csvreader)
    [print(f"CSV Header: {csv_header}")]
    
    for row in csvreader:
        Votes.append(row[0])

        #candidates
        Candidate = row[2]
        #set list of non repeating candidates and their corresponding vote count
        if Candidate not in Candidates:
            Candidates.append(row[2])
            Candidate_Votes[Candidate] = 0
        
        Candidate_Votes[Candidate] +=1

   

output_file = 'Analysis/PyPoll.txt'
with open(output_file, "w", newline="") as datafile:

    print("Election Results")
    print("-------------------------------")
    print("Total Votes:", len(Votes))
    print("--------------------------------")


    datafile.write("Election Results\n")
    datafile.write("-------------------------------\n")
    datafile.write(f"Total Votes:  {len(Votes)}\n")
    datafile.write("--------------------------------\n")

    
    
    for Candidate in Candidates:
        Percentage = (round(float(Candidate_Votes[Candidate]) / len(Votes), 2)*100)

        
        print(f"{Candidate}: {Percentage} ({Candidate_Votes[Candidate]})")
        datafile.write(f"{Candidate}: {Percentage} ({Candidate_Votes[Candidate]})\n")
        

        if Winning_Votes < Candidate_Votes[Candidate]:
            Winning_Votes = Candidate_Votes[Candidate]
            Winner = Candidate

    print("----------------------------------------")
    print("Winner: ", str(Winner))
    print("----------------------------------------")

    datafile.write("----------------------------------------\n")
    datafile.write(f"Winner:  {Winner}\n")
    datafile.write("----------------------------------------")


datafile.close()










        
    
