# Open sample sequence file and name it sSeq
sSeq = open("seq.txt", "r")
# Read sSeq and save the contents in a string called Sample
Sample = sSeq.read()

# This function will format input text into a usable form
def Clean_Input (Sample_Sequence):
    # Removes all spaces from Sample_Sequence and put the result in string Sample_Sequence_1
    Sample_Sequence_1 = Sample_Sequence.replace(" ", "")

    # Will let us check later if the file included a protein name
    Name = False

    # Checks to see if the file has a name in the first line, and if so caries out the following operations
    if Sample_Sequence_1[0] == ">":
        # Splits off the first line of the string
        Split = Sample_Sequence_1.split("\n",1)
        # Makes a new string equal to the first line of the document
        PN = str(Split[0])
        # Removes the ">" from the line and saves it as the Protein_Name
        Protein_Name = PN.replace(">","")
        # Puts the remainder of the text into a string called Sample_Sequence_2
        Sample_Sequence_2 = Split[1]
        Name = True
    else:
        # If the file does not have a protein name in the first line, simply set Sample_Sequnce_2
        # equal to all of Sample Sequence_1
        Sample_Sequence_2 = Sample_Sequence_1

    # Removes all of the line breaks in the sequence
    Sample_Sequence_3 = Sample_Sequence_2.replace("\n", "")

    # This if else statement returns the sequence and the protein name, unless there is no protein name, in which case
    # it returns only sequence
    if Name == True:
        return [Sample_Sequence_3,Protein_Name]
    else:
        return [Sample_Sequence_3];

# This function will use the code containing input file to translate nucleotide sequence to AA sequence
def Decipher(sequence1):

    # Open codon-to-AA file and name it Codon
    Codon = open("code.txt", "r")
    # Read Codon and save the contents in a string called Codon_Code
    Codon_Code = Codon.read()

    # Creates string that will eventually be returned by this method, at which point it will contain the
    # deciphered AA sequence of the protein
    AA_Sequence = ""

    # Creates an array where each entry is one line from the code file
    Lines = Codon_Code.split("\n")

    # Creates four new strings where each is an entry from the array
    One = Lines[0]
    Two = Lines[1]
    Three = Lines[2]
    Four = Lines[3]

    # Creates four arrays, each with two entries - the first entry is before the "=" and the second is after the "="
    AA_I = One.split("=")
    B1_I = Two.split("=")
    B2_I = Three.split("=")
    B3_I = Four.split("=")

    # Creates four strings that are equal to the first entry from each of the arrays.
    # This is a cleaned form of each line from the original document
    AA_Identity = AA_I[1]
    B1_Identity = B1_I[1]
    B2_Identity = B2_I[1]
    B3_Identity = B3_I[1]

    # Removing trailing white space in the AA_Identity string will allow us to have an accurate number for how many
    # different AA we need to check in order to translate the codons
    AA_Identity.rstrip()

    # AA_Num stores the number of amino acid identities that must be searched through
    AA_Num = len(AA_Identity)

    # This loop will collapse the three base identity strings into a list of codons
    Codon_List = []

    # This loop meshes together the three base identity strings into a list of codons
    for i in range (0,AA_Num):
        Codon_List.append(B1_Identity[i] + B2_Identity[i] + B3_Identity[i])

    # Takes first index of input list and creates a string called sequence
    sequence = sequence1[0]
    # Finds the location of the first start codon
    Start_Position = sequence.find("ATG")

    # Creates a substring of the nucleotide sequence starting at the first start codon
    Open_Reading = sequence[Start_Position:]

    # Divides the open reading frame by three to find the number of codons that will need to be read (rounds to int)
    Loop_Length = int(len(Open_Reading)/3)

    # Initiates booleans and counters for the following loop
    Found_Codon = False
    Place_Counter = 0

    # This is the loop that will actually do the decoding
    for i in range(0,Loop_Length):
        # The Index_Counter will be reset to 0 at the beginning of each outer loop iteration
        Index_Counter = 0

        # For each set of three nucleotides, the list of codon codes will be searched through for the
        # corresponding AA until a match is found.
        while Found_Codon == False:

            # If a match is found, the letter representing the AA identity is added to the AA sequence
            # and the boolean Found_Codon is changed to true, ending the while loop
            if Open_Reading[Place_Counter:Place_Counter+3] == Codon_List[Index_Counter]:
                AA_Sequence += AA_Identity[Index_Counter]
                Found_Codon = True
            # Otherwise, the index being checked is increased by one
            else:
                Index_Counter += 1
        # After the corresponding amino acid for this codon is found the location in the sequence is
        # moved forward by three, keeping the reading frame in frame
        Place_Counter += 3
        # Because we have moved forward to a new, untested codon the Found_Codon is returned to false
        Found_Codon = False

    # Here we locate the index of the first '*' character in the AA_Sequence. This is the first stop codon
    Stop_Position = AA_Sequence.find("*")

    # We trim off everything after the first stop codon and return the finalized sequence
    AA_Sequence = AA_Sequence[0:Stop_Position]
    return AA_Sequence;

# Transforms the input files into usable formats
Cleaned = Clean_Input(Sample)

# Prints a deciphered version of the input sequences, along with a protein name if applicable
Decipher_Output = Decipher(Cleaned)

if len(Cleaned) == 2:
    print("The amino acid sequence of " + Cleaned[1] + " is \n" + Decipher_Output)
else:
    print("The amino acid sequence of this protein is \n" + Decipher_Output)
