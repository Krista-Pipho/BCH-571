# Creates a file in which to write the results of our manipulations
output = open("output1.FASTA", "w+")

# Open comma delimited data file and name it dataset
dataset = open("ss-dos.txt", "r")

# Read dataset and save the contents in a string called data
data = dataset.read()

# Removes trailing white space at the end of lines
data.rstrip()

# Creates an array called data_lines, where each entry is one line from the data string
data_lines = data.split("\n")

# The last \n in the string was at the end of the last line of data, so the very last entry in the list is empty.
# Here we remove this last, empty entry
del data_lines[(len(data_lines)-1)]

# This imports the 'math' set of functions. We will use this later for our calculations
import math

# This loop iterates over every index in the list made up of data lines
for line in data_lines:
    # Here we initialize several variables we will use later on in calculation
    Sum = 0
    Sum_Square = 0
    Standard_D = 0
    Mean = 0
    # Here we take the current data line and split it at every coma, generating a new list called data_points
    # in which every entry should consist of only one number
    data_points = line.split(",")
    # We set the variable length equal to the length of the data points list
    length = len(data_points)

    # This loop iterates over every entry in the data_points list
    for datum in data_points:
        # The single number in each datum is changed in type from a string to a float and saved as datum_num
        datum_num = float(datum)
        # Here we add each datum one at a time to a sum count that runs the length of the line
        Sum += datum_num
        # Here we square each datum and add these squares to a sum that runs the length of the line
        Sum_Square += (datum_num * datum_num)
    # After looping through every datum in this line we calculate the standard deviation of all of this line's numbers
    Standard_D = math.sqrt((length * Sum_Square) - (Sum * Sum)) / length
    # We also calculate the mean of this line's numbers
    Mean = Sum/length
    # For each line in the data set one mean and one SD is written into the output file on its own line
    output.write(str(Mean) + "," + str(Standard_D) + "\n")

output.close()
dataset.close()







