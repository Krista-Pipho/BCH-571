# Separate FASTA file into component sequences, each in own FASTA file : Lab 1.2

# Open original FASTA file and name it dualFASTA
dualFASTA = open("lab-1-input.FASTA", "r")

# Read dualFASTA and save the contents as a string called dualsequence
dualsequence = dualFASTA.read()

# Creates a new string, the same as dualsequence but with all dashes removed.
cleandual = dualsequence.replace("-", "")

# Identifies the first instance of >Seq2 and returns the position of the ">" as an integer
transition = cleandual.find(">Seq2")

# Creates a substring from cleandual starting at index 0 and ending at the transition between the two sequences
sequence1 = cleandual[0:transition]

# Creates a substring from cleandual starting at the transition between the two sequences and going until the last index
sequence2 = cleandual[transition:]

# Creates a file variable, and assigns it a newly created file named output#.FASTA
w1 = open("output1.FASTA", "w+")
w2 = open("output2.FASTA", "w+")

# Populates the newly created files with our strings
w1.write(sequence1)
w2.write(sequence2)




