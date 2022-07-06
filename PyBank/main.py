 # import the csv and as modules
import csv
import os



# load the file to read the survey data
inputFile = os.path.join("Resources","budget_data.csv")

# output file location for financial records analysis
outputFile = os.path.join("Analyist","financialrecordsanalysis.txt")


# set the variable
monthTotal = 0
budgetTotal = 0
change = []
date = []

# open and read the file
with open(inputFile,"r") as recordsFile:
    # reader
    csvreader = csv.reader(recordsFile)

    # header row 
    header = next(csvreader)
    # first row
    firstrow = next(csvreader)

    # increment the total month count 
    monthTotal += 1
    # add to the total budget 
    budgetTotal += float(firstrow[1])
    # set initial  budget 
    initialBudget = float(firstrow[1])



    # break out the rest into a row
    for row in csvreader:
        # increment total month count
        monthTotal += 1

        # add into total budget 
        budgetTotal += float(row[1])



        # net change calulations
        netChange = float(row[1]) - initialBudget

        
        # add to the change list
        change.append(netChange)

        # fisrt month change occured 
        date.append(row[0])


        # update inital budget 
        initialBudget = float(row[1])


    # avg net change / month
    averageChange = sum(change) / len(change)

    greatestIncrease = [date[0], change[0]]
    greatestDecrease = [date[0], change[0]]

    # calculate the greatest and least change of the index using loop
    for m in range(len(change)):
        # calculate greatest increase & decrease
        if(change[m] > greatestIncrease[1]):
            # if the value is more than the greatest increase then it becomes new increase
            greatestIncrease[1] = change[m]
            # month update
            greatestIncrease[0] = date[m]


        if(change[m] < greatestDecrease[1]):
            # if the value is more than the greast decrease then it becomes new decrease 
            greatestDecrease[1] = change[m]
            # month update 
            greatestDecrease[0] = date[m]


#  start generating the output
output = (
    f"Financial Data Analysis \n"
    f"------------------------\n"
    f"Total Months = {monthTotal} months\n"
    f"Average Change = ${averageChange:,.2f}\n"
    f"Greast Increase = {greatestIncrease[0]},(${greatestIncrease[1]:,.2f})\n"
    f"Greast Decrease = {greatestDecrease[0]},(${greatestDecrease[1]:,.2f})"
)

# print output
print(output)


# export to text fiele
with open(outputFile,"w") as textFile:
    textFile.write(output)



