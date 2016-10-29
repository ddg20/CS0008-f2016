PD = 0 # partial distance
PTN = 0 # partial total number
TTD = 0 # total total distance
TTNL = 0 # total total number of lines

file = input("Input file name: ")

def main():
    while(file and file != "QUIT" and file != "Q" and file != "quit" and file != "q"): # input validation
        fh = open(file, 'r') # opens data file to read
        processFile(fh) # calls processFile function
        PD, PTN = processFile(fh)
        printKV("PARTIAL #" + str(PTN)) # calls printKV function
        printKV("PARTIAL D" + str(PD))
        fh.close() # closes file
        TTD += PD # adds total distance
        TTNL += PTN # adds total number of lines
        file = input("Input next file name or type quit or q to exit: ")

def processFile(fh):
    for line in fh:
        line = line.rstrip("\n") # removes new line
        temp = line.split(",") # splits two elements through comma
        dist = temp[1] # takes 2nd element from list (python starts counting at 0, so second element is "1")
        dist = float(temp[1]) # converts number from string to float
        PD += dist # sums up the partial distance
        PTN += 1 # tallies the partial number of lines

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