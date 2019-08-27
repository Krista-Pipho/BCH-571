# Imports Biopython function that we will use
from Bio import SeqIO

# Uses the Biopython function to open and process the sequence fasta
for seq_record in SeqIO.parse("seq.txt","fasta"):

    # Sets string sequence equal to one of the output variables from the function containing the sequence from the fasta
    sequence = seq_record.seq

# Finds the position of the first start codon
place = sequence.find("ATG")

# Makes a new substring starting at the start codon
open_reading = sequence[place:]

# Uses another Biopython function to decode sequence we got out of the fasta file, going only until the first stop codon
protein = open_reading.translate(to_stop = True)

# Prints the translated protein sequence
print(protein)