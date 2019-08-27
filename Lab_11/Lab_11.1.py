# For choosing random numbers
import random
# For receiving information from the command line
import sys


# This function swaps the ith and jth position of an input array
def swap(in_array, i, j):
    # Temp holds the ith value while the ith position is replaces with the jth position
    temp = in_array[i]
    in_array[i] = in_array[j]
    # After this is done the jth position is set equal to temp
    in_array[j] = temp
    # Returns the modified array
    return in_array


# This function randomly shuffles an input string
def shuffle(input):
    # Declares empty array
    in_array = []
    # This loop fills the array, one letter of the string to each index
    for i in range(0, len(input), 1):
        in_array.append(input[i])
    # This loop looks at each position in the string, and as it sweeps over it switches it with another random position
    for i in range(0, len(in_array), 1):
        # Chooses random position for j
        j = random.randint(0, len(in_array)-1)
        # Feeds current position i, random position j, and current state of the array to the swap function
        in_array = swap(in_array, i, j)
    out_str = ""
    for i in range(0, len(in_array), 1):
        out_str = out_str + in_array[i]
    print(out_str)


shuffle(sys.argv[1])




