# PyBank

# -------------------------------INSTRUCTIONS -------------------------------------------------------------------------

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
# The dataset is composed of two columns: `Date` and `Profit/Losses`.
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

#  * The total number of months included in the dataset
#  * The net total amount of "Profit/Losses" over the entire period
#  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#  * The greatest increase in profits (date and amount) over the entire period
#  * The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#  '''text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  '''

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# -----------------------------------------------------------------------------------------------------------------------

# import csv and os libraries
import csv
import os

# set path to read file.
readFilePath = os.path.join('.', 'Resources', 'budget_data.csv')

#set path to write (output) file.
writeFilePath = os.path.join('.', 'Analysis', 'budget_analysis_output.txt')

# Create blank list 'months' to store unique month values
months = []

# Create variable 'netTotal' to keep running total of net total profit/losses.
netTotal = 0

# Create variable 'previousAmt' to store previous month's profit/losses as loop iterates.
previousAmt = None

# Create blank list to store month-to-month profit/losses.
changeAmts = []

# open read file
with open(readFilePath) as budgetFile:

	# Specify variable that holds contents and delimiter
	rows = csv.reader(budgetFile, delimiter = ',')

	# Skip the header.
	next(rows)

	# Loop through rows to find unique month values.
	for row in rows:
	
		# If value is NOT in the 'months' list...
		if row[0] not in months:
			
			# ... then append it to the 'months' list.
			months.append(row[0])
		
		#keep a running total of profit/losses
		netTotal = netTotal + int(row[1])
	
		# if 'previousAmt' is NOT null (i.e, this conditional start from row 3)...
		if previousAmt is not None:

			# ... Then subtract current row amount from previous row amount...
			# ... and append to 'changeAmts'.
			changeAmts.append(float(row[1]) - previousAmt)
		
		# Assign current amout to 'previousAmt' for next iteration.
		previousAmt = float(row[1])

# Assign max of month-to-month change to 'mostProfitableAmt'
mostProfitableAmt = int(max(changeAmts))

# Find index of greatest increase and store in variable.
mostProfitableAmtIndex = changeAmts.index(mostProfitableAmt)

# Find corresponding month using months list.
mostProfitableMonth = months[mostProfitableAmtIndex + 1]

# Find index of greatest decrease and store in variable.
leastProfitableAmt = int(min(changeAmts))

# Find index of greatest decrease and store in variable.
leastProfitableAmtIndex = changeAmts.index(leastProfitableAmt)

# Find corresponding month using months list.
leastProfitableMonth = months[leastProfitableAmtIndex + 1]

# Store formatted results in variable 'textOutput'.
textOutput = (f'''
Financial Analysis
----------------------------
Total Months: {len(months)}
Total: ${netTotal}
Average Change: ${round(sum(changeAmts) / len(changeAmts), 2)}
Greatest Increase in Profits: {mostProfitableMonth} (${mostProfitableAmt}) 
Greatest Decrease in Profits: {leastProfitableMonth} (${leastProfitableAmt})''')

# Print results to the console.
print(textOutput)

# open write (output) file
with open(writeFilePath, 'w') as outputFile:
    
	# write results to analysis (output) file.
	print(textOutput, file = outputFile)