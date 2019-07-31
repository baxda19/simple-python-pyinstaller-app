import pyautogui
import time
import csv
import pyperclip
import msvcrt
import sys
import traceback

file = input("Press enter CSV file name:")

with open(file) as f:
	reader = csv.reader(f)
	next(reader)
	data = []
	for row in reader:
		data.append(row)

#defines row_count variable for total count
file2 = open(file)
row_count = len(file2.readlines()) - 1


print (data)
print (row_count)

#confirm correct data has been imported
while True:
	reply = input("Press y to continue")
	print (reply)
	if reply == 'y':
		break

#function for converting a string to a bool
def str2bool(v):
	if v == 'Yes':
		return True
	elif v == 'No':
		return False
	else:
		return False

#defining a function to copy a value, paste it then tab
def pastetab(copyvalue):
	pyperclip.copy(copyvalue)
	pyautogui.hotkey('Ctrl','v')
	pyautogui.hotkey('tab')

#defining a function to copy a value, paste it then tab with delay
def pastetabwait(copyvalue, delay):
	pyperclip.copy(copyvalue)
	pyautogui.hotkey('Ctrl','v')
	time.sleep(delay)
	pyautogui.hotkey('tab')

#defining a function to type a value, paste it then tab with delay
def typewait(typevalue, delay, typeinterval):
	pyautogui.typewrite(typevalue, interval=typeinterval)
	time.sleep(delay)
	pyautogui.hotkey('tab')

#defining a function to press space if true, and then tab
def spacetab(testvalue):
	if testvalue == True:
		pyautogui.hotkey('space')
		pyautogui.hotkey('tab')
	else:
		pyautogui.hotkey('tab')


#define error function
def show_exception_and_exit(exc_type, exc_value,tb):
	traceback.print_exception(exc_type, exc_value, tb)
	input("Press key to exit.")
	sys.exit(-1)

sys.excepthook = show_exception_and_exit

def copycheckvalue(valuetobe):
	pyautogui.hotkey('Ctrl', 'c')
	checkcode = pyperclip.paste()
	if checkcode != valuetobe:
		print("Clipboard: " + checkcode)
		print("Value To Be: " + valuetobe)
		pyautogui.alert("Check Inventory Item Window is ready, Once ready press any key to continue")

#define counting variables
i = int(input("What row should the script start from?"))
f = 0
	
pyautogui.hotkey('alt', 'tab')

while i < row_count:
	
	Personnel = data[i][0]
	FirstName = data[i][5]
	LastName = data[i][6]
	Title = data[i][7]
	Company = data[i][8]
	Phone = data[i][9]
	Direct = data[i][10]
	Fax = data[i][11]
	Mobile = data[i][12]
	Email = data[i][13]
	Address = data[i][14]
	City = data[i][15]
	State = data[i][16]
	Postal = data[i][17]
	Type = data[i][18]
	Status = data[i][19]
	
	
	pyautogui.click(x=1019, y=349)
	pyautogui.click(x=1019, y=349)
	time.sleep(2)

	print(Personnel)
	print(FirstName)
	print(LastName)
	print(Title)
	print(Company)
	print(Phone)
	print(Direct)
	print(Fax)
	print(Mobile)
	print(Email)
	print(Address)
	print(City)
	print(State)
	print(Postal)
	print(Type)
	print(Status)
	
	
	#scrippted actions 
	pastetab(FirstName)
	pyautogui.press(['tab'])
	pyautogui.press(['tab'])
	pastetab(LastName)
	Acccode = "MAJEV" + str(i)
	pastetab(Acccode)
	pastetab(Title)
	typewait(Company, 0.5, 0.05)
	pyautogui.press(['tab'])
	pastetab(Address)
	typewait(City, 0.5, 0.05)
	typewait(State, 0.5, 0.05)
	pastetab(Postal)
	pyautogui.press(['tab'])
	typewait(Type, 0.5, 0.05)
	pastetab(Phone)
	pastetab(Direct)
	pastetab(Fax)
	pastetab(Mobile)
	pastetab(Email)
	pyautogui.press(['tab'])
	pyautogui.press(['tab'])	

	#move to next row of data & reset coloumn search for new data set
	i += 1
	f = 0

	pyautogui.alert("Confirm Item Description is Correct \n" + "Row " + str(i) + " Out of " + str(row_count))


	#complete form
	pyautogui.hotkey('enter')

while True:
	pyautogui.hotkey('tab')
	reply = input("Press y to continue")
	print (reply)
	if reply == 'y':
		break