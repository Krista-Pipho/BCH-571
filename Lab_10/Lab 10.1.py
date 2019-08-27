# Declares the string containing the sequence of coin flip results
StringX = "HHHHTTTTHHHHHHHTHTHTHTHHHHTHHTTTTHHTHHT"
# Initializes TP (probability of remaining on the same coin)
TP = .9

# This function outputs the most likely series of coins used to produce the observed series of H/T results
def FairCasino(x,TP):
    # Generates two appropriately sized arrays that will hold coin use probabilities. VF is fair and VB is biased
    VF = [0]*(len(StringX)+1)
    VB = [0]*(len(StringX)+1)
    # Sets the zero index equal to .5 for each
    VF[0] = .5
    VB[0] = .5
    # This loop finds the most likely coin at each position and saves the associated probability
    for i in range (1,len(StringX)):
        # This if/else sets the probability of that outcome for the biased coin
        if StringX[i] == "H":
            Px = .75
        else:
            Px = .25
        # These statements determine the maximum (most likely) course of action and saves the resulting probability
        VF[i] = .5 * max(TP * VF[i-1],(1-TP)*VB[i-1])
        VB[i] = Px * max(TP * VB[i-1],(1-TP)*VF[i-1])
    # Initializes the empty output string
    pi = ""
    # Sets I to the index of the final entry (len - 1)
    i = len(StringX) - 1
    # This if/else compares the probabilities saved in the ends of the two strings and picks the biggest one and adds
    # the corresponding coin to the output string
    if VF[i] > VB[i]:
        state = "F"
        pi = pi+"F"
    else:
        state = "B"
        pi = pi+"B"
    # This loop moves backwards through the two lists and determines what step was most likely to have come before
    while (i > 0):
        # The current coin in use is .9 probability to stay in use because of the TP value, this pair of if/else
        # statements decides what coin was most likely used for the last flip given the outcome of the flip and
        # the current state. Ultimately it adds whichever was most likely to the beginning of the pi string
        if state == "F":
            if VF[i] ==.5 * TP * VF[i-1]:
                state = "F"
                pi = "F" + pi
            else:
                state = "B"
                pi = "B" + pi
        else:
            if StringX[i] == "H":
                Px = .75
            else:
                Px = .25
            if VB[i] == Px * TP * VB[i-1]:
                state = "B"
                pi = "B" + pi
            else:
                state = "F"
                pi = "F" + pi
        # Iterates i down by one
        i = i-1
    # Returns the final list of most likely coins used on each flip
    return pi

# Runs FairCasino on StringX
print(FairCasino(StringX,TP))

# If TP was changed to a lower value it would make it less detrimental to switch coins. If TP around .5
# the likely coin used for each toss can be seen to correspond closely with the outcome of the toss. If TP
# is much lower than .5 then the likely coin just alternates each toss regardless




