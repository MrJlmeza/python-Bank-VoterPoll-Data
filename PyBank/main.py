#-------import modules
import os
import csv

#--------------set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#----------create lists to store data
Profits_Losses = []
Monthly_changes = []
Dates = []
Greatest_Increase_Date = ""
Greatest_Decrease_Date = ""


#-----------read csv files using csv module
with open(csvpath) as csvfile:
    #-----------CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    #set and fix header row prior to loop
    csv_header = next(csvreader)
    [print(f"CSV Header: {csv_header}")]
    
    #-----Loop through csv
    for row in csvreader:
        #begin obtaining values for lists and variables
        Dates.append(row[0])
        Profits_Losses.append(float(row[1]))

    print("Financial Analysis")
    print("----------------------------------")
    print("Total Months:", len(Dates))
    print("Net Total: $", sum(Profits_Losses)) 

        
        
    for i in range(1, len(Profits_Losses)):
        
        #obtain profit changes between months, store values in list
        Monthly_changes.append(Profits_Losses[i] - Profits_Losses[i-1])
        
        #Use Values in montly changes list to calculate average change
        Average_Change = sum(Monthly_changes) / len(Monthly_changes)

        #Use Values in in monthly changes list to determine greatest gain and loss and corresponding dates
        Greatest_Profit_Increase = max(Monthly_changes)
        Greatest_Increase_Date = str(Dates[Monthly_changes.index(max(Monthly_changes))])
        Greatest_Profit_Decrease = min(Monthly_changes)
        Greatest_Decrease_Date = str(Dates[Monthly_changes.index(min(Monthly_changes))])
    #------------------Create print statements
    print("Average Change: $", round(Average_Change))
    print("Greatest Increase in Profits: ", Greatest_Increase_Date, "$", Greatest_Profit_Increase,")")
    print("Greatest Decrease in Profits: ", Greatest_Decrease_Date, "($", Greatest_Profit_Decrease,")")

output_file = 'Analysis/PyBank.txt'
with open(output_file, "w", newline="") as datafile:

    #write print statements into output text file
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------------\n")
    datafile.write(f"Total Months: {len(Dates)}\n")
    datafile.write(f"Net Total: $ {sum(Profits_Losses)}\n")
    datafile.write(f"Average Change: $ {round(Average_Change)}\n")
    datafile.write(f"Greatest Increase in Profits:  {Greatest_Increase_Date} (${Greatest_Profit_Increase})\n")
    datafile.write(f"Greatest Decrease in Profits:  {Greatest_Decrease_Date} (${Greatest_Profit_Decrease})\n")

datafile.close()
    

    

        
        
        