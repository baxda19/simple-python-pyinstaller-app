import pyautogui, csv, pyperclip
from time import sleep
from ConfigParser import SafeConfigParser

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
    for row in csv_reader:
        print row

print "CSV File read to Pandas DataFrame"



print "Shutting Down...."
