#
# MN: file header with user, instructor, course info is missing
#


# MN: if you define your variables here, they become global variables and 
#     are not visible inside any of the functions, including main where you use them
#     They should be move in side main
#PD = 0 # partial distance
#PTN = 0 # partial total number
#TTD = 0 # total total distance
#TTNL = 0 # total total number of lines

# MN: why do you ask the file name outside the main function
#     if you ask the file name here, it will not be defined inside the main function
#file = input("Input file name: ")

# MN: what does this function do?
def main():
    # MN: here is where your accumulators should be defined
    PD = 0 # partial distance
    PTN = 0 # partial total number
    TTD = 0 # total total distance
    TTNL = 0 # total total number of lines
    # MN: here is where your should ask for the file name
    file = input("Input file name: ")
    while(file and file != "QUIT" and file != "Q" and file != "quit" and file != "q"): # input validation
        fh = open(file, 'r') # opens data file to read
        #
        # MN: in the followign 2 statments you are calling the same function twice, but you capture the output only on the second one
        #     with the first pass, all the line sof the files are processes
        #     with the second call, the file pointer is already at the end of the file
        #     so no line is process, and the output is a nice zero
        #processFile(fh) # calls processFile function
        PD, PTN = processFile(fh)
        # MN: printKV accept 2 mandatory arguments in input
        #     the way you call the function here, you are passing in only one, that is a string.
        #printKV("PARTIAL #" + str(PTN)) # calls printKV function
        printKV("PARTIAL #", str(PTN)) # calls printKV function
        #printKV("PARTIAL D" + str(PD))
        printKV("PARTIAL D", str(PD))
        fh.close() # closes file
        TTD += PD # adds total distance
        TTNL += PTN # adds total number of lines
        file = input("Input next file name or type quit or q to exit: ")
    # 
    # MN: here you have processed all your files
    #     you should be printing your overall totals.

# MN: what does this function do?
def processFile(fh):
    # MN: you need to initialize your local accumulators
    PD = 0
    PTN = 0
    for line in fh:
        line = line.rstrip("\n") # removes new line
        temp = line.split(",") # splits two elements through comma
        #
        # MN: here you are redefining the same variables 2 times, you just need the second statment
        dist = temp[1] # takes 2nd element from list (python starts counting at 0, so second element is "1")
        dist = float(temp[1]) # converts number from string to float
        PD += dist # sums up the partial distance
        PTN += 1 # tallies the partial number of lines
    # 
    # MN: once you have processed all the lines in the file
    #     your should pass back the total distance run and the total number of lines for the file
    #     otherwise they will not be available in main where you are supposed to use them
    return PD, PTN


# MN: what does this function do?
def printKV(key, value, klen = 0): # prints key and value in consistent format
    kl = max(len(key), klen)
    if isinstance(value, str): # prints 20 spaces if string
        fs = '20s'
    elif isinstance(value, float): # prints 10 spaces with 3 decimals if float
        fs = '10.3f'
    elif isinstance(value, int): # prints 10 spaces if integer
        fs = '10s'
    else: # prints 20 spaces if anything else
        fs = '20s'
    print(format(key, str(kl) + 's') + ":" + format(value, fs))

main() # calls main function
