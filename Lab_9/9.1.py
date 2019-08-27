def Needleman_Wunsch(vSEQ,wSEQ,M,N,I):
    score = []
    v = len(vSEQ)
    w = len(wSEQ)
    for i in range(0,v+1,1):
        col = []
        score.append(col)
        for j in range (0,w+1,1):
            score[i].append(0)
    for i in range(0,w+1,1):
        score[0][i] = -i
    for i in range(0,v+1,1):
        score[i][0] = -i
    for i in range(1,v+1,1):
        for j in range(1,w+1,1):
            if vSEQ[i-1] == wSEQ[j-1]:
                match = M
            else:
                match = N
            score[i][j] = max(match + score[i-1][j-1], match + score[i-1][j] + I, score[i][j-1] + I)
    #for col in score:
    #    print(col)
    Alignment_v = ""
    Alignment_w = ""
    i=v
    j=w
    while(i>0 or j>0):
        if(i>0 and j>0):
            if(vSEQ[i-1] == wSEQ[j-1]):
                match = M
                print(str(i) + "  " + str(j))
            else:
                match = N
            if score[i][j] == score[i-1][j-1] + match:
                Alignment_v = vSEQ[i-1] + Alignment_v
                Alignment_w = wSEQ[j-1] + Alignment_w
                i= i-1
                j = j-1
            elif (score[i][j] == score[i-1][j] + I):
                Alignment_v = vSEQ[i-1] + Alignment_v
                Alignment_w = "-" + Alignment_w
                i = i-1

            else:
                Alignment_v = "-" + Alignment_v
                Alignment_w = wSEQ[j-1] + Alignment_w
                j = j-1
        elif (i>0):
            print(str(i) + "    " + str(j))
            Alignment_v = vSEQ[i-1] + Alignment_v
            Alignment_w = "-" + Alignment_w
            i = i-1
        else:
            Alignment_v = "-" + Alignment_v
            Alignment_w = wSEQ[j-1] + Alignment_w
            j = j-1
    print("done")
    return Alignment_v,Alignment_w
first = "ACUUAGCUAAAACGUUUGGUUCAAAACAUUUGCUUGCUGUCUUGGCAUAACAUCAAUAAAGGCAUAAACAUCGCAAAACAAUGGUUAUAUAUAAAUGGCUAUGAGGAUGGUUUUAGUACGUAGGCGUUGCGGAACUUCGGUUCAGAUAGAGCAAUGAAUCGUGCAUGCUAGGAAAACUGACCACACGCAGUUGGCAGCCCUAGUAUCUUUCGAUAGAUUUCCAUACCUCCGCGAUC"
second = "ACUUAGCCUAUACACUAUGUUGGAGAGAGACGCUUGCUACCUAGGCAUAAUGUGAAUUAGGUAUAAACAUCGUGGUUGUAAACUUGAGUGGGUUUUAGUACGGUAUGCGUGAUUACUUCGUAAUCAUGAAUCGUGCAUGCUAGUGGGGUUUGGCCUCCACUAGUAUCUUUGAAGAUUUUCCUUCCUCAGCGAUC"
print(Needleman_Wunsch(first,second,1,-.5,-1))




'''    

      else  
         Alignment_v ← “‐“+ Alignment_v 
         Alignment_w ← wj + Alignment_w 
         j← j – 1 
return Alignment_v,Alignment_w 
One tricky aspect is setting up the 2D score array.  In python, this is a list of lists.  Here is python code for 
making the list of lists: 
#create a list of lists that is indexed for v and then w
#this 0-indexed list of lists has 0 for the nucleotide before the
start
infinity = 10000
score=[]
for nucleotide in v:
 row = [infinity]*(len(w)+1)
 score.append(row)
row = [infinity]*(len(w)+1)
score.append(row)
Run the algorithm with the sequences: 
v=   
ACUUAGCUAAAACGUUUGGUUCAAAACAUUUGCUUGCUGUCUUGGCAUAACAUCAAUAAAGGCAUAAACAUCGCAAAACAAUGGUUAUAUAUAAAUGGCUAUGAGGAUGGUUUUAGUACGUAGGCGUUGCGGAACUUCGGUUCAGAUAGAGCAAUGAAUCGUGCAUGCUAGGAAAACUGACCACACGCAGUUGGCAGCCCUAGUAUCUUUCGAUAGAUUUCCAUACCUCCGCGAUC 
w=     
ACUUAGCCUAUACACUAUGUUGGAGAGAGACGCUUGCUACCUAGGCAUAAUGUGAAUUAGGUAUAAACAUCGUGGUUGUAAACUUGAGUGGGUUUUAGUACGGUAUGCGUGAUUACUUCGUAAUCAUGAAUCGUGCAUGCUAGUGGGGUUUGGCCUCCACUAGUAUCUUUGAAGAUUUUCCUUCCUCAGCGAUC 
And with M = 1, N = ‐0.5, I = ‐1 

'''