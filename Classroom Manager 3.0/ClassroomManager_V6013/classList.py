#initialising imports
from tkinter import *
from tkinter import ttk
import classTab
import database
import os
try: #Try except must be in all PIL calls
	from PIL import *
except:
	os.popen('pip install Pillow')

#creation of class specific buttons that are available on main tab... dynamically created
def classButtons(root, frame1, teacherId, notebook):
	def tabCommand(root, classArray, buttonNo, teacherId, notebook): #tab selection backend commands
		buttonArray[buttonNo].config(state='disabled')
		classTab.createTab(root, classArray, buttonNo, teacherId, notebook, buttonArray[buttonNo])
		numTabs = len(notebook.tabs())
		notebook.select(numTabs - 1)
		return

	f = ttk.Style()  # creation of standard UI style
	f.configure('TFrame', background='white')

	#creation of new frame
	classFrame = ttk.Frame(frame1, style='TFrame')
	classFrame.config(width=300, height=250, border=1, relief='sunken')
	classFrame.place(x=280, y=130)

	numClasses = database.requestNumClasses_teacherId(teacherId) #retrieves the number of classes

	classArray = []
	buttonArray = []
	buttonNoArray = []
	for v in range(0, numClasses): #preloads variables for the number of classes to be dynamically created
		classArray.append("")
		buttonArray.append("")
		buttonNoArray.append("")

	nameArray = []

	i = 0
	buttonRow = 0
	buttonColumn = 0
	while i < (numClasses): #based on the number of classes, for each create a button in the Main tab
		classArray[i] = database.requestClass_teacherId(teacherId, i)
		(buttonArray[i]) = classArray[i][1]
		nameArray = buttonArray

		buttonArray[i] = ttk.Button(classFrame, text=nameArray[i], command=lambda m=i: tabCommand(root, classArray[m],
																								  m, teacherId, notebook))
		buttonArray[i].grid(row=buttonRow, column=buttonColumn, padx=5, pady=5)
		buttonRow = buttonRow + 1
		if buttonRow == 4: #some formatting for different amounts of buttons... columns of four
			buttonRow = 0
			buttonColumn = buttonColumn + 1
		if buttonColumn >= 3: #limit on the amount of classes
			print("Unexpected amount of classes.") #feedback for database managers / administrators (not for user)
			break
		i = i + 1