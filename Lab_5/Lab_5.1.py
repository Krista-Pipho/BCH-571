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

# Initializes a set that will be filled with all occurring codon pairs.
Codon_Pairs = set()

# We now loop through each codon pair in each ORF, not including start and stop codons
for ORF in Clean_ORF:
    # Initializes the position in each orf as 3 to skip start codon
    position = 3
    # This makes sure we only search up to the length of the orf, but do not look at the last codon
    while(position < len(ORF)-9) == True:
        Codon_Pairs.add(str(ORF[int(position):int(position + 6)]))
        # Moves the reading position forward by 3 after adding the current codon pair
        position += 3

# Prints out the number of unique codon pairs found across all ORFs
print(len(Codon_Pairs))
