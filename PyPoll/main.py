import os
import csv
input_file_csv = os.path.join("/users/bunni","Desktop","election_data.csv")
output_result = os.path.join(".","txt_file")
total_votes = 0
# candidates, and votes ###
candidates_options = [ ] 
candidates_votes = {}
winner = " "
winner_votes = 0
total_votes_at_the_poll = 0
### reading the csv file and adding candidates and their number of votes in the dictionary 
with open(input_file_csv) as electrion_data_from_poll:
    reader = csv.reader(electrion_data_from_poll)
    # Read the header
    header = next(reader)
    for row in reader:
        #print(". ",end=""),
        candidates_name = row[2]
        total_votes_at_the_poll+=1
        # Create the key : Candidate name and value: the number of votes
        if candidates_name not in candidates_options:
            candidates_options.append(candidates_name)
        # creating the dictionary key with value 0
        candidates_votes[candidates_name] = 0
        candidates_votes[candidates_name] = candidates_votes[candidates_name]+ 1
with open(output_result,"w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes_at_the_poll}\n"
    )
    print (election_results)
#Determine the winner by looping through the votes
# get keys from the dictionary candidates_votes
    for candidate in candidates_votes:
        votes = candidates_votes.get(candidate)
        print ("candidate",candidate)        
        vote_percentage = float(votes)/float(total_votes_at_the_poll) * 100
        
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate
        # candidates voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output,end="")
        txt_file.write(voter_output)
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winner}\n"
        f"----------------------\n")
    
    print (winning_candidate_summary)



    txt_file.write(winning_candidate_summary)


    
    