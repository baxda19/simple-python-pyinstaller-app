import pyautogui, csv, pyperclip
from time import sleep
from ConfigParser import SafeConfigParser

#Functions
def printTable(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))

#Intro
print "Project:     MAJEV - Inventory Updater"
print "Author:      Jacob Baxter Davis"
print "Date:        01/08/2019"
print "Version:     0.1"
print "Purpose:     To be used to update the MAJEV EBMS Inventory for the 2019 event season"
print "Config:      Taken from 'config.ini'"
print "===================================================================================="
print ""

print "Reading Config File..."
parser = SafeConfigParser()
parser.read('config.ini')

print "Configuration:"

#File
print "[File]"
File = parser.get('File', 'File')
FileLocation = parser.get('File', 'Location')
print "File:            ", File
print "FileLocation:    ", FileLocation

#Data
print "[Data]"
StartRow = parser.get('Data', 'StartRow')
print "StartRow:        ", StartRow

#Mouse
print "[Mouse]"
FirstClickX = parser.get('Mouse', 'FirstClickX')
FirstClickY = parser.get('Mouse', 'FirstClickY')
print "FirstClickX:     ", FirstClickX
print "FirstClickY:     ", FirstClickY

#Typing
print "[Typing]"
TypeInterval = parser.get('Typing', 'TypeInterval')
Delay = parser.get('Typing', 'Delay')
print "TypeInterval:    ", TypeInterval
print "Delay:           ", Delay
print ""

#Loading CSV File
CSVFile = FileLocation + File
print "Reading CSV File: ",CSVFile, " ..."

with open(CSVFile) as f:
    csv_reader = csv.DictReader(f)
    printTable(csv_reader)


print "CSV File read to Pandas DataFrame"



print "Shutting Down...."
