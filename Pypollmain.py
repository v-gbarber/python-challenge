import os
import csv
#output file
election_data= os.path.join('.','resources', 'election_data.csv')
print(os.getcwd())

#Variables
votes_cast=0
county =[]
list_candidates=[]
amount_won={}
percentage_won=0
winning_candidate=[]
winning_votes=0

#open csv
with open(election_data) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter= ",")
    header = next(csvfile)
    print(f'Header: {header}')

    for row in csv_reader:
        votes_cast += 1

        if row[2] not in list_candidates:
            list_candidates.append(row[2])
            amount_won[row[2]]=0
            amount_won[row[2]]+=1  
        else: 
            amount_won[row[2]]+=1 
print(amount_won)
for candidate in amount_won:
    votes=amount_won.get(candidate)
    vote_percentage=votes / votes_cast * 100
    print(f'{candidate}: {votes} {vote_percentage}%')
    if votes > winning_votes:
        winning_votes=votes
        winning_candidate = candidate



#Percentage 
#Pypoll_Analysis

print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {votes_cast}")
print(f"------------------------")
print(f'Winner: {winning_candidate}')
print(winning_votes)
file_to_save = os.path.join("analysis", "Pypoll_code.txt")
with open (file_to_save, "w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f"Total Votes: {votes_cast}\n")
    txtfile.write(f"----------------------\n")
    txtfile.write(f'Winner: {winning_candidate}\n')
    txtfile.write(f'{candidate}: {votes} {vote_percentage}% \n')
    txtfile.write(f'{amount_won}\n')
    txtfile.write(f'{winning_votes}\n')

