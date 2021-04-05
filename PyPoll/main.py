
import os
import csv 
from collections import Counter 

election_csv = os.path.join('..', 'PyPoll','Resources', 'PyPoll_Resources_election_data.csv')



with open(election_csv, newline='') as csvfile:
	
	csvreader = csv.reader(csvfile, delimiter=",")
	
	csv_header = next (csvreader,None)	

# Lists to election data 

	voter_id = []
	candidates = []

# the total number of votes cast

	for row in csvreader:
			voter_id.append(row[0])
			candidates.append(row[2])

			total_votes = len(voter_id)
		
	
# A complete list of candidates who received votes
	
	list_candidates = set(candidates)
	
	
# The total number of votes each candidate won			

	v_Khan = int(candidates.count("Khan"))	
	v_Li = int(candidates.count("Li"))	
	v_OTooley = int(candidates.count("O'Tooley"))	
	v_Correy = int(candidates.count("Correy"))	
	
# The percentage of votes each candidate won 

	Khan_percent =v_Khan/total_votes 
	Li_percent = v_Li/total_votes 
	OTooley_percent = v_OTooley/total_votes 
	Correy_percent = v_Correy/total_votes 



# Summary of result 

candidates_list = ['Khan', 'Correy', 'Li','OTooley']

votes_count =[(v_Khan),(v_Correy),(v_Li),(v_OTooley)]

votes_percentage =["{:.3%}".format(Khan_percent),"{:.3%}".format(Correy_percent),"{:.3%}".format(Li_percent),"{:.3%}".format(OTooley_percent)]

result = zip(candidates_list,votes_percentage,votes_count)

result_list = list(result)



# The winner of the election based on popular vote 
	
votes_counter = Counter(candidates)
winner = votes_counter.most_common(1)		



# Print result to Terminal


print(f"Election Results")
print(f"------------------------------------------------------")
print(f"Candidates List: {list_candidates}")
print(f"------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------------------------------------")

print(*result_list, sep="\n")
print(f"------------------------------------------------------")

print(f"Winner: {winner}")
print(f"------------------------------------------------------")






#Print result to text file
output_path = os.path.join('..' ,'PyPoll','Analysis','election result.txt')

with open (output_path, 'w', newline="") as textfile:
	
	
	print(f"Election Results", file=textfile)

	print(f"------------------------------------------------------",file=textfile)

	print(f"Candidates List: {list_candidates}",file=textfile)

	print(f"------------------------------------------------------",file=textfile)

	print(f"Total Votes: {total_votes}",file=textfile)

	
	print(f"------------------------------------------------------",file=textfile)

	print(*result_list, sep="\n", file=textfile)

	print(f"------------------------------------------------------",file=textfile)

	print(f"Winner: {winner}", file=textfile)

	print(f"------------------------------------------------------",file=textfile)	


	

	

	

	


	