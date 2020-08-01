#initialising imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import studentFunction
import tkinter as tk
import add
import fail
import os
import database
try: #Try except must be in all PIL calls
	from PIL import *
except:
	os.popen('pip install Pillow')

# For each class when the specified class button is pressed a tab is created containing
# most of the system's functionality
def createTab(root, classArray, buttonNo, teacherId, notebook, button):
	def setup(root, classArray, buttonNo, teacherId, notebook, button): #setup tab itself
		(tab) = classArray[1]
		tab = ttk.Frame(notebook)
		notebook.add(tab, text="{}".format(classArray[1]))
		encapsulate = ttk.Frame(tab)
		encapsulate.config(height=600, width=800)
		encapsulate.pack()

		def on_configure(event): #scrollbar functionality
			canvas.configure(scrollregion=canvas.bbox('all'))

		# create canvas with scrollbar
		canvas = Canvas(encapsulate)
		canvas.config(height=560, width=770, background='white', relief=RIDGE, bd=0, highlightthickness=0)
		canvas.pack(side=LEFT)
		scrollbar = Scrollbar(encapsulate, command=canvas.yview)
		scrollbar.pack(side=RIGHT, fill='y')
		canvas.configure(yscrollcommand=scrollbar.set)

		#update scrollregion after starting 'mainloop' when all widgets are in canvas
		canvas.bind('<Configure>', on_configure)

		frame = Frame(canvas)
		frame.config(background='white')
		canvas.create_window((0, 0), window=frame, anchor='nw')

		classTitle = ttk.Label(frame, text="{}".format(classArray[1]), background='white', font=('Calibri', '20'))
		classTitle.pack(pady=10, padx=20)

		numStudents = database.requestNumStudents_classArray(classArray[0]) #requests the number of students in class

		def addAssignment(): #adds an assignment to all students in the class
			assignmentAddButton.config(state='disabled')
			add.addAssignment(classArray)
			tab.destroy()
			createTab(root, classArray, buttonNo, teacherId, notebook, button)
			numTabs = len(notebook.tabs())
			notebook.select(numTabs - 1)
			return
		def subAssignment(): #removes the last assignment from all students in the class
			assignmentSubButton.config(state='disabled')
			add.subAssignment(classArray)
			tab.destroy()
			createTab(root, classArray, buttonNo, teacherId, notebook, button)
			numTabs = len(notebook.tabs())
			notebook.select(numTabs - 1)
			return
		def closeCurrTab(button): #closes the tab
			button.config(state='normal')
			tab.destroy()
			return

		#Utility frame setup...

		utilFrame = Frame(frame, background='gray97', bd=1, relief=SUNKEN) # utility frame for the teacher to manage
		utilFrame.pack(fill=X, pady=2, padx=5)							   # some functionality of the class

		teacherName, null1, null2 = database.requestTeacher_teacherId(teacherId)

		#basic class info
		nameInfo = ttk.Label(utilFrame, text="Teacher: {}".format(teacherName), background='gray97')
		nameInfo.grid(row=0, column=0, pady=5, padx=10)
		classSize = ttk.Label(utilFrame, text="Students: {}".format(numStudents), background='gray97')
		classSize.grid(row=0, column=3, pady=5, padx=10)

		#spaceholders
		fill1 = ttk.Label(utilFrame, text="", background='gray97')
		fill1.grid(row=0, column=2, pady=10, padx=90)
		fill2 = ttk.Label(utilFrame, text="", background='gray97')
		fill2.grid(row=0, column=4, pady=10, padx=90)

		#buttons within utility frame
		assignmentAdd = ttk.Label(utilFrame, text="Add an Assignment: ", background='gray97')
		assignmentAdd.grid(row=0, column=5, pady=5, padx=1)
		assignmentAddButton = tk.Button(utilFrame, height=1, width=2, text="+", command=addAssignment)
		assignmentAddButton.grid(row=0, column=6, pady=5, padx=(0, 5))
		assignmentSub = ttk.Label(utilFrame, text="Remove last Assignment: ", background='gray97')
		assignmentSub.grid(row=1, column=5, pady=5, padx=1)
		assignmentSubButton = tk.Button(utilFrame, height=1, width=2, text='-', command=subAssignment)
		assignmentSubButton.grid(row=1, column=6, pady=5, padx=(0, 5))
		closeTab = tk.Button(utilFrame, text="EXIT {}".format(classArray[1]), command=lambda: closeCurrTab(button))
		closeTab.grid(row=1, column=0, pady=(0, 15))

		#dynamically creates the frames for students of the class
		student = []
		studentFrame = []
		for i in range(0, numStudents):
			student.append("")
			studentFrame.append("")

		i=0
		while i < numStudents:
			student[i] = database.requestStudentClass_classArray(classArray[0], i)
			studentFrame[i] = student[i]

			studentFrame[i] = Frame(frame, background='gray97', bd=1, relief=SUNKEN)
			studentFrame[i].pack(fill=X, pady=2, padx=5)

			studentFunction.populate(studentFrame[i], student[i])
			i=i+1
		#for the amount of students a frame is created then calls a student module that creates all frame functions

	setup(root, classArray, buttonNo, teacherId, notebook, button)