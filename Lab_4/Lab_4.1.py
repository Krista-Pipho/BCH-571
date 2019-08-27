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

# Imports a combination generating tool from itertools
from itertools import product

# Generates a list containing every possible 6 nucleotide combination
comb = list(product('ATCG', repeat = 6))

# Initializes a dictionary to hold all of the formatted codon pairs
Codon_Pairs = {}

# Formats each entry in comb (a list) into a string of 6 characters and makes it a new entry in the dictionary of pairs
for Codon_Pair in comb:
    makestring = Codon_Pair[0]+Codon_Pair[1]+Codon_Pair[2]+Codon_Pair[3]+Codon_Pair[4]+Codon_Pair[5]
    Codon_Pairs [makestring] = 0

# This loop counts the occurrences of each codon pair
for pair in Codon_Pairs:
    # Initializes/resets the codon instance count and position after testing each pair
    count = 0
    position = 3

    # For each pair, we check over every ORF in the Clean_ORF file and add up all of the pair matches found
    for ORF in Clean_ORF:

        # This makes sure we only search up to the length of the orf, but do not look at the first or last codon
        while(position < len(ORF)-9) == True:
            # Adds one to the count if a match is found
            if ORF[int(position):int(position+6)] == pair:
                count += 1
            # Moves the reading position forward by 3 after checking each pair
            position += 3
        # Returns the position to 0 after each ORF
        position = 0
    # Sets the key of each pair equal to the count that was found across all ORFs
    Codon_Pairs[pair] = count

for key in Codon_Pairs.keys():
    if Codon_Pairs[key] != 0:
        print(key + " : " + str(Codon_Pairs[key]))