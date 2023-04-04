import os
import csv

#variable to track in election data 
total_vote_counter = 0 

candidate_options = []

candidate_votes = {}

winning_candidate = ""

winning_count = 0 

#open election data csv and turn into a list of dictionaries 
with open("Resources/election_data.csv", 'r') as file:

    csvreader = csv.reader(file, delimiter= ",")
#read header    
    header = next(csvreader)

#loop through eachh row and count the total number of votes
    for row in csvreader:

        total_vote_counter = total_vote_counter + 1
#get the candidates name from each row
        candidate_name = row[2]
#If the candidate name doesn't match the previous name then add it to the list candidate options
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
#start tracking the votes each candidate recieved             
            candidate_votes[candidate_name] = 0 
#add a vote to the candidates name 
        candidate_votes[candidate_name] += 1
#made sure code was running     
#print(total_vote_counter)
#print(candidate_votes) 

#print out election results
    print("Election Results")

    print("----------------------")

    print(f'Total Votes: {total_vote_counter}')
#calculate and print each candidates name, % votes, and total votes each one recieved 
    for candidate_name in candidate_votes:

        print(f'{candidate_name}: {(candidate_votes[candidate_name]/total_vote_counter)*100}% ({candidate_votes[candidate_name]})')

        if candidate_votes[candidate_name] > winning_count:

           winning_count = candidate_votes[candidate_name]  

           winner = candidate_name

    print("--------------------")    
    print(f"Winner: {winner}")
#export election results to a text file
with open("Analysis/election_data_finished.txt", 'w') as file:
            
    file.write("Election Results\n")

    file.write("----------------------\n")

    file.write(f'Total Votes: {total_vote_counter}\n')

    for candidate_name in candidate_votes:

        file.write(f'{candidate_name}: {(candidate_votes[candidate_name]/total_vote_counter)*100}% ({candidate_votes[candidate_name]})\n')

        if candidate_votes[candidate_name] > winning_count:

           winning_count = candidate_votes[candidate_name]  

           winner = candidate_name

    file.write("--------------------\n")    
    file.write(f"Winner: {winner}\n")
