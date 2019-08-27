# Imports subprocess function to interface with R
import subprocess
# Imports itertools for generating a list of all column combinations
from itertools import combinations

# Declares the subprocess that will interact with R for part 1
R_Call = subprocess.call(r'C:\"Program Files"\R\R-3.4.2\bin\Rscript Exercise_3.R', shell = True)
print(R_Call)


# Declares the subprocess that will interact with R for part 2
Call_R = subprocess.call(r'C:\"Program Files"\R\R-3.4.2\bin\Rscript Exercise_2.R', shell = True)

# Opens the data file
CDcsv = open("condition_data.csv",'r')
# Creates an output file and sets the mode to write
Out_File = open ("Final_Output","w")

# Uses itertools to generate a list populated with all combinations
comb = list(combinations((0,1,2,3,4,5,6), 2))

# Declares a list that will be a list of each line, which itself is a list
Columns = []

# This loop reads lines of the data file one at a time and separates each column into an index,
# then adds the resulting list to the list named columns
for lines in CDcsv:
    row = CDcsv.readline()
    conditions = row.split("\t")
    Columns.append(conditions)

# This loops through every combination of columns that we generated earlier and stored in 'comb'
for pair in comb:
    # The temporary python out file is opened here so that it is overwritten for each pair
    tmp_out = open('tmp_python_out.csv', 'w')
    # We add column headers to the empty file, so that its format fits what the R program wants as input
    tmp_out.write("A" + "\t" + "B")
    # This loops through every processed line that we saved in 'Columns"
    for con in Columns:
        # This tells the program to ignore the empty line that I didn't know how to remove another way,
        # Only allowing the next step if the line had data for all 7 columns
        if len(con) == 7:
            # Here we add the data from the current line, but only the two columns comprising the pair, to the output
            tmp_out.write(str("\n" + con[pair[0]].rstrip() + "\t" + con[pair[1]].rstrip()))
    # Now that the columns comprising the pair have their data point from every line written in the temp out file,
    # the R program is called to process it
    Call_R = subprocess.call(r'C:\"Program Files"\R\R-3.4.2\bin\Rscript Exercise_3.R', shell=True)
    # Now we retrieve the results of the R call by opening the R output file and reading it into a string
    R_Out = open("tmp_R_out.txt", "r")
    R_Outread = R_Out.read()
    # We search the string for the p value
    position = R_Outread.find("p-value =")
    # We know from examining the output that the value of "p-value" begins 10 indices after the p in 'p-value',
    # so we make a string that starts there and goes to the end of the output
    temp_string = R_Outread[int(position + 10):]
    # We split this string at the new lines - the p-value is the last portion of a line
    temp_list = temp_string.split("\n")
    # We set the value equal to the zeroth index of the split - this ensures that the reported p-value will include
    # all characters comprising the p-value, which is of potentially variable character length
    value = temp_list[0]
    # We add a formatted line to the final output for each pair of columns
    Out_File.write("\n" + "Combination of Conditions " + str(pair[0] + 1) + " and " + str(pair[1] + 1) + ": p = " + value)
