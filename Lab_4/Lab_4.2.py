# Importing the re module
import re

# Open ORFs file and name it ORF.txt
ORF_txt = open("Scer_100genes.nt.txt", "r")
# Read ORF.txt and save the contents in a string called ORFS
ORFS = ORF_txt.read()

# Create a list where each entry is one line from the string ORFS
ORF_List = ORFS.split("\n")
# Delete the last entry which is empty because nothing follows the last new line character
del ORF_List[len(ORF_List)-1]

# Initializes a new list that will hold cleaned orfs
Clean_ORF = []
# Initializes a list that will contain ORF names
Names = []
# For each item in the list ORF_List, split the line at ':'. The first half will be the name and the second
# half the sequence. We add all of the names to one list and all of the cleaned ORF sequences to the other
for ORF in ORF_List:
    cut = ORF.split(":")
    Names.append(cut[0])
    Clean_ORF.append(cut[1])

# Here we make a zip to iterate over both names and clean orfs in tandem
for name,seq in zip(Names,Clean_ORF):
    # Here we use an re function to find every instance of the codon pair and put its location into the locations list
    Locations = re.finditer(r"CGACGA",seq)
    # Here we make sure that every output line will begin with the name of the gene we are searching
    output = str(name)
    # For each of the locations we found we will now determine if it is in frame or out of frame using the mod operation
    for loc in Locations:
        frame = loc.start()%3
        # Here we will add the location and frame information to the output for each gene sequence
        if frame == 1 or 2:
            output += str(", " + str(loc.start()) + " is out of frame")
        if frame == 0:
            output += str(", " + str(loc.start()) + " is in frame")
    # If no instances of the codon pair were found and nothing was added to the output string we add "none found"
    if output == str(name):
        output += ", None Found"
    # And finally we print the formated output, one line for each Clean_ORF tested
    print(output)