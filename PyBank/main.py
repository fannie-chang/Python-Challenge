
# Import os module to read CSV file

import os
import csv


# Path to collect data from the PyBank folder

budget_csv = os.path.join('..' ,'PyBank','Resources','budget_data.csv')

# Open the file 

with open(budget_csv, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

# Skip the first row of the CSV file
	csv_header = next (csvreader, None)


 #Lists to budget data 

	date=[]
	profit_losses=[]
	trend_change = []
	

	total_net_amount = 0 
	total_trend_change = 0
	
		
# Loop through the data

	for row in csvreader:
		
		date.append(row[0])
		profit_losses.append(row[1])
		
# Calculate total months 

		total_months = list(date)
		num_months = len(total_months)
	
# Calculate total net amount

		total_net_amount = total_net_amount + int(row[1])
	
# Loop through data for profit_losses list

	for i in range(len(profit_losses)-1):
			
# Calculate average trend changes	(current value - previous value)

		trend_change.append(int(profit_losses[i+1]) - int(profit_losses[i]))

		total_trend_change = total_trend_change + (int(profit_losses[i+1]) - int(profit_losses[i]))

		trend_average = round(total_trend_change / (len(total_months)-1),2)
		
# Calculate greatest increase and decrease 

		greatest_increase = max (trend_change)
		greatest_decrease = min (trend_change)
		
# Find date for greatest increase and decrease		

		max_date_index = trend_change.index(greatest_increase)
		max_date = date[max_date_index +1] 

		min_date_index = trend_change.index(greatest_decrease)
		min_date = date[min_date_index +1]
	
# Print result 		
		
	print(f"Financial Analysis ")
	print(f"-------------------------------- ")
	print(f"Total Months: {num_months}")
	print(f"Total:${total_net_amount} ")
	print(f"Average Change: ${trend_average}")
	print(f"Greatest Increase in Profits: {max_date}  ${greatest_increase}")
	print(f"Greatest Decrease in Profits: {min_date}  ${greatest_decrease}")
				



#Print result to text file
output_path = os.path.join('..' ,'PyBank','Analysis','financial_analysis.txt')

with open (output_path, 'w', newline="") as textfile:
	
	print(f"Financial Analysis ", file=textfile)
	print(f"--------------------------------", file=textfile )
	print(f"Total Months: {num_months}", file=textfile)
	print(f"Total:${total_net_amount} ", file=textfile)
	print(f"Average Change: ${trend_average}", file=textfile)
	print(f"Greatest Increase in Profits: {max_date}   ${greatest_increase}", file=textfile)
	print(f"Greatest Decrease in Profits: {min_date}   ${greatest_decrease}", file=textfile)
				
	

	