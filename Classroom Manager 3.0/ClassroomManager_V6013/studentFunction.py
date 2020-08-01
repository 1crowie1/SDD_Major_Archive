#initialising imports
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import database
import fail
try: #Try except must be in all PIL calls
	from PIL import *
except:
	os.popen('pip install Pillow')

def populate(Sframe, student): #populate the student frame with it's functionality
	def loadAssignment(i, labelArray, entryArray, curRow, curColumn): #loads assignment and its database link
		labelArray[i] = ttk.Label(Sframe, text="Assessment {}".format(str(i+1)), background='gray97')
		labelArray[i].grid(row=curRow, column=curColumn, padx=25, pady=(5, 0))
		assignmentId = database.requestAssignmentId_classIdTaskNum(student[2], (i+1))
		mark = database.requestStudentClassAssignmentMark_studentClassIdAssignmentId(student[0], assignmentId[0])
		entryArray[i] = ttk.Entry(Sframe, width=5)
		entryArray[i].grid(row=(curRow+1), column=curColumn, pady=(0, 5))
		entryArray[i].insert(0, mark[0])
	def submitMarks(): #sumbits the marks by inserting into data fields in sqlite database
		numMarks = len(entryArray)
		i = 0
		while i < numMarks: #for each of the marks that are retrieved save their value
			try:
				mark = int(entryArray[i].get())
				if mark >= 0 and mark <= 100: #constraints
					assignment = database.requestAssignmentId_classIdTaskNum(student[2], (i+1))
					database.updateStudentMark_studentClassIdTaskNumMark(student[0], assignment[0], mark)
				else:
					fail.fail("Enter a mark from 0 to 100") #exception
			except:
				fail.fail("Enter a mark from 0 to 100") #exception
			i = i + 1
		return
	def submitBNotes(): #submit behavioural notes into the database
		note = bNotes.get("1.0", END)
		done = database.updateStudentClassBehaviour_studentClassId(note, student[0])
		if done == False:
			fail.fail("Behaviour note must not exceed 1000 characters")
		return

	#requesting data from database on student and setting up frame
	studentId, studentName = database.requestStudent_studentId(student[1])
	studentInfo = ttk.Label(Sframe, text="{}".format(studentName), background='gray97', font=('Calibri', 12))
	studentInfo.grid(row=0, column=0, padx=5, pady=5)

	numTasks = database.requestTaskNum_classId(student[2])
	labelArray = []
	entryArray = []
	curRow = 1 #current row and current column done for dynamic formatting
	curColumn = 0
	i = 0
	while i < numTasks: #load the tasks in
		labelArray.append(str(i))
		entryArray.append(labelArray[i])
		loadAssignment(i, labelArray, entryArray, curRow, curColumn)
		curColumn = curColumn + 1
		if curColumn == 6:
			curColumn = 0
			curRow = curRow + 2
		i = i+1

	curRow = curRow+3
	subMarks = tk.Button(Sframe, text="SAVE MARKS", command=lambda: submitMarks())
	subMarks.grid(row=(curRow), column=0, pady=(5, 15))

	curRow = curRow+1
	bNoteLab = ttk.Label(Sframe, text="Behaviour Notes:", background='gray97')
	bNoteLab.grid(row=curRow, column=0)

	curRow = curRow+1
	bNotes = tk.Text(Sframe, background='white', height=5)
	bNotes.grid(row=curRow, column=0, columnspan=7, sticky=W+E, padx=40)

	curRow = curRow+1
	subBNote = tk.Button(Sframe, text="SAVE BEHAVIOUR NOTES", command=lambda : submitBNotes())
	subBNote.grid(row=curRow, column=0, columnspan=7, pady=(5, 15), padx=(0, 500))
	noteDb = database.requestNote_studentClassId(student[0])
	bNotes.insert("1.0", noteDb[0][0]) #inserts behaviour notes retrieved from database



