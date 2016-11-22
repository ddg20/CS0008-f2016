totalFiles = 0   # initialize total files variable
totalLines = 0   # initialize total lines variable
totalDistance = 0   # initialize total distance variable
totalParticipants = 0 # initialize total participants variable
data = []      # initialize the data list
dictionary = {} # initialize dictionary
i = 0  # initialize index variable
file = input("Enter the name of the file to be read: ") # prompt user to input file to be read
while(file != 'q' and file != 'Q' and file != "quit" and file != "Quit" and file != "QUIT"): # tests whether or not file should be read
    fh = open(file, 'r') # opens file and assigns to file handler
    for line in fh: # for loop runs through each line in file
        data.append(line.strip('\n').split(',')) # strips new line and splits name from distance
        while(line != ''):
            totalDistance += float(data[i][1]) # calculates total distance through accumulator variable
            i += 1 # index increases
        totalLines += 1 # adds up all of the lines
    del data[0] # removes "name distance" from beginning of each file

    fh.close() # closes file

    file = input("Enter the name of another file to be read or type 'q' or 'quit' to stop: ") # asks user to input next file or quit program
    totalFiles += 1 # adds up all of the files

minDistance = min(data) # calculates minimum distance
maxDistance = max(data) # calculates maximum distance
maxParticipant = max([data]) # returns participant with max distance
minParticipant = min([data]) # returns participant with min distance
totalParticipants = totalLines - totalFiles # calculates total number of participants

print(data) # outputs everything
print("\nNumber of Input Files read    :  " + str(totalFiles))
print("Total number of lines read    :  " + str(totalLines))
print()
print("Total Distance Run            :  " + format(totalDistance, '.5f'))
print()
print("Max Distance Run              :  " + format(maxDistance, '.5f'))
print("  by participant              :  " + maxParticipant)
print("Min Distance Run              :  " + format(minDistance, '.5f'))
print("  by participant              :  " + minParticipant)
print()
print("Total number of participants  :  " + str(totalParticipants))
print("Number of participants ")
print("with multiple records         :  ")