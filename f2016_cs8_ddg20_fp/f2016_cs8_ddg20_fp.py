#
# HEADER????
#


class Participant:

    # properties
    # name of the participant
    name = "unknown"
    # total distance run by the participant
    distance = 0
    # total number of runs by the participant
    runs = 0

    # initializer methods
    def __init__(self, name, distance=0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0:
            # set distance
            self.distance = distance
            # set number of runs
            self.runs = 1

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1

    # addDistances method
    def addDistances(self, distances):
        # loops over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1

    # return the name of the participant
    def getName(self):
        return self.name

    # return the total distance run computed
    def getDistance(self):
        return self.distance

    # return the number of runs
    def getRuns(self):
        return self.runs

    # stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')

    # convert to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

# function getDataFromFile(file)
# read all the lines from the file, remove first line (header) and split all the others in name and distance
# insert a dictionary with name and distance in output list

def getDataFromFile(file):
    # initialize output list
    output = []
    # read file line by line
    for line in open(file,'r'):
        # exclude first line that is the header
        # we can recongize it because it contains the word "distance"
        if "distance" in line:
            # skip line
            continue
        # remove \n ending the line and split line at ","
        temp1 = line.rstrip('\n').split(',')
        # use try/except to avoid unhendled errors
        try:
            # append record to output list in the form of a dictionary with 2 keys: name and distance
            # remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            print('Invalid row : '+line.rstrip('\n'))
    # return data records
    return output

# ask for master file from user
masterFile = input("Please provide master file : ")

# read master file and extract data files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
except:
    print("Impossible to read master file or invalid file name")
    exit(1)
# end try/except

# read data from data files
#
# rawData is a list of all the records from each data file
# according to posting #43 of http://stackoverflow.com/questions/4344017/how-can-i-get-the-concatenation-of-two-lists-in-python-without-modifying-either
# sum() can concatenate lists in a list if it is provided with an empty list as initial value
rawData = sum([getDataFromFile(file) for file in dataFiles],[])
#
# number of files read
numberFiles = len(dataFiles)

# total number of lines read
# this is equivalent to the sum of the second item in each item of rawData
totalLines = len(rawData)

#
# total number distance run by every participant
# this is equivalent of the sum of the "distance" element of the items in the uniqueListdata
totalDistanceRun = sum([item['distance'] for item in rawData])

#
# compute distance run for each participant and how many records we have for each one of them
# initialize all the accmulators
# dictionary with one element for each participant whose value is
# the list of all the distances found in data for the participant
participants = {}

# loops on all the records
for item in rawData:
    # check if the names has already been found previously or if it is new
    # if it is new, initialize elements in the accumulators
    if not item['name'] in participants.keys():
        participants[item['name']] = Participant(item['name'])
    # insert distance in the list for this participant
    participants[item['name']].addDistance(item['distance'])
# end for

# initialize accumulators
# minum distance run with name
minDistance = { 'name' : None, 'distance': None }
# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# appearences dictionary
appearences = {}
#
# computes the total distance run for each participant iterating on all the participants
for name, object in participants.items():
    # get the total distance run by this participant
    distance = object.getDistance()
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance

    # get number of runs, aka apparences from participant object
    participantAppearences = object.getRuns()

    # check if we need to initialize this entry
    if not participantAppearences in appearences.keys():
        appearences[participantAppearences] = []
    appearences[participantAppearences].append(name)

# compute total number of participant
totalNumberOfParticipant = len(participants);

# compute total number of participants with more than one record

totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])

# set format strings
integer = '5d'
float = '12.5f'
string = '20s'

# provide requested output
print("Number of Input files read   : " + format(numberFiles, integer))
print("Total number of lines read   : " + format(totalLines, integer))
print("")
print("Total distance run           : " + format(totalDistanceRun, float))
print("")
print("Max distance run             : " + format(maxDistance['distance'], float))
print("  by participant             : " + format(maxDistance['name'], string))
print("")
print("Min distance run             : " + format(minDistance['distance'], float))
print("  by participant             : " + format(minDistance['name'], string))
print("")
print("Total number of participants : " + format(totalNumberOfParticipant, integer))
print("Number of participants")
print(" with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords, float))
print("")

# create output file
# MN: re-using code from somebody else is fine, but you should always personalize it!!!
outputFile = "f2016_cs8_man8_a3.output.csv"
# open file for writing
fh = open(outputFile, 'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for name, object in participants.items():
    # write line in file
    fh.write(object.tocsv() + '\n')
# close files
fh.close()


