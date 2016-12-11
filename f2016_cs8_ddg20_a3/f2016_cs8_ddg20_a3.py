#
# MN: header with user, intructor and course info is missing
#
# Notes:
# MN: please, please, please do not use comments at the end of the code lines
#     it makes it really hard to read it
# MN: you are not reading the master file to find out which data files you need to read
#

totalFiles = 0   # initialize total files variable
totalLines = 0   # initialize total lines variable
totalDistance = 0   # initialize total distance variable
totalParticipants = 0 # initialize total participants variable
data = []      # initialize the data list
# MN: why do you define dictionary and you are not using it?
dictionary = {} # initialize dictionary
i = 0  # initialize index variable
#
# MN: you need to define an additional dictionary to store the participants and their total distance run
participants= {}
# MN: initialize variables to find min and max
minDistance = 100000
maxDistance = 0
maxParticipant = ''
minParticipant = ''

# MN: first you should ask the user which is the master list files that you need to read
master_file = input('Enter the name of the master file : ')

# MN: than you should read the name of the data files from the master file
#     store data file names in a list
data_files = []
fh = open(master_file)
for file in fh:
    data_files.append(file.strip('\n'))
fh.close()


# MN: now you are ready to read the data files
#     you do not need to ask the user for file names and check if the user wants to exit
#file = input("Enter the name of the file to be read: ") # prompt user to input file to be read
#while(file != 'q' and file != 'Q' and file != "quit" and file != "Quit" and file != "QUIT"): # tests whether or not file should be read
#
# MN: loop on all the data file names that your read above
for file in data_files:
    fh = open(file, 'r') # opens file and assigns to file handler
    for line in fh: # for loop runs through each line in file
        # MN: you need to skip the file headers
        #     one way to do it is as follow:
        #     check if the line contains the word distance
        if 'distance' in line:
            continue
        #
        # MN: it is better to assign the list to a temp variable because we need to re-use it multiple times
        #data.append(line.strip('\n').split(',')) # strips new line and splits name from distance
        temp = line.strip('\n').split(',')
        # convert second element aka distance to float
        temp[1] = float(temp[1])
        data.append(temp)
        # MN: why do you test for empty line and you loop on it?
        #     if the line is not empty you enter in an infinite loop and you will never get out.
        #     if you want to be sure that line is empty, you should test it were you test for the header
        #while(line != ''):
        #    totalDistance += float(data[i][1]) # calculates total distance through accumulator variable
        #    i += 1 # index increases
        #
        # MN: you can avoid to use index i, because the element that you are looking for is always at the end of the list data
        # MN: use temp variable
        #totalDistance += float(data[i][1]) # calculates total distance through accumulator variable
        totalDistance += float(temp[1])
        i += 1 # index increases
        totalLines += 1 # adds up all of the lines

        # MN: update participants total distance
        if temp[0] in participants.keys():
            # MN: the user was already found
            participants[temp[0]] += temp[1]
        else:
            # MN: first time we find this name
            participants[temp[0]] = temp[1]

        # MN: compute min and max
        # MN: only issue is that this if statements will compute min and max on single records and
        #     not on the total distance run by the participant
        if minDistance > temp[1]:
            minDistance = temp[1]
            minParticipant = temp[0]
        if maxDistance < temp[1]:
            maxDistance = temp[1]
            maxParticipant = temp[0]

    # MN: this would work if you would not try to transfomr the second element in a float
    #     that's the error that you got.
    #     everytime you are reading the header, you are trying to convert "distance" in a float and python raise an error
    #del data[0] # removes "name distance" from beginning of each file

    fh.close() # closes file

    # MN: you do not need this because the file name comes from the list read above
    #file = input("Enter the name of another file to be read or type 'q' or 'quit' to stop: ") # asks user to input next file or quit program
    totalFiles += 1 # adds up all of the files

# MN: you cannot compute min and max this way
#     you are applying the min/max function to a list of list
#     you need to apply them to a list of numbers, in our case are the distances
# MN: as it is now, your best bet is to comput min and max in the for loop where you read files line by line
#minDistance = min(data) # calculates minimum distance
#maxDistance = max(data) # calculates maximum distance
# MN: are you sure about the following 2 statments?
#maxParticipant = max([data]) # returns participant with max distance
#minParticipant = min([data]) # returns participant with min distance




# MN: the total number of participants cannot be computed this way
#     beacuse you would not keep tab of multiple records for the same participants
#totalParticipants = totalLines - totalFiles # calculates total number of participants

# MN: why do you print all the data on screen? If it is for debug porpuses, it is fine,
#     but you should comment it or remove it when you submit the script
#print(data) # outputs everything
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

# MN: producing the output file is missing