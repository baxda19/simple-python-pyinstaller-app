import pyautogui, csv, pyperclip
from time import sleep
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

File = parser.get('File', 'File')
FileLocation = parser.get('File', 'Location')

print File
print FileLocation