import pyautogui, csv, pyperclip
from time import sleep

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
    if v == 'x':
        return True
    elif v == '':
        return False
    else:
        return False

#defining a function to type a value
def typewait(typevalue, delay, typeinterval):
    pyautogui.typewrite(typevalue, interval=typeinterval)
    sleep(delay)

#define counting variables
i = int(input("What row should the script start from?"))
    
pyautogui.hotkey('alt', 'tab')

while i < row_count:
    
    Update = data[i][6]

    if str2bool(Update):
        Space_Description = data[i][0]
        Type = data[i][1]
        Code = data[i][3]
        Keep = data[i][4]
        Update = data[i][6]
        
        print(Space_Description)
        print(Code)
        print(Type)

        pyautogui.click(x=236, y=230)
        pyautogui.click(x=236, y=230)

        typewait(Code, 1, 0.1)
        pyautogui.hotkey('enter')

        pyperclip.copy(Type)

        pyautogui.alert("Click when you are ready for next")
        pyautogui.hotkey('alt', 'tab')

    i += 1

while True:
    pyautogui.hotkey('tab')
    reply = input("Press y to continue")
    print (reply)
    if reply == 'y':
        break