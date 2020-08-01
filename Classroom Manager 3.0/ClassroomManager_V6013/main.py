#initialising imports
from tkinter import *
from tkinter import ttk
from datetime import datetime
import sys
import os
import classList
import database
try: #Try except must be in all PIL calls
	from PIL import *
except:
	os.popen('pip install Pillow')

def mainP(teacherId):
	def getTeacher(teacherId): #get the teacher info using teacherId
		name, pic, timetableId = database.requestTeacher_teacherId(teacherId)
		return name, pic, timetableId

	def sysLogout(root): #logout of program
		global buttonPressed
		buttonPressed = True
		root.destroy()

	def createTimetable(timetableId): #get timetable fields
		timetableId, dayOne, dayTwo, dayThree, dayFour, dayFive = database.requestTimetable_timetableId(timetableId)

		def getDay(day): #get days based on timetable fields
			dayArray = ["", "", "", "", "", ""]  # preloaded for 6 periods of day timetable
			dayArray[0], dayArray[1], dayArray[2], dayArray[3], dayArray[4], dayArray[5] = database.requestDay_day(day)
			return dayArray[0], dayArray[1], dayArray[2], dayArray[3], dayArray[4], dayArray[5]

		dayOneArray = ["", "", "", "", "", ""] #preloaded for 6 periods of day timetable
		dayTwoArray = ["", "", "", "", "", ""]
		dayThreeArray = ["", "", "", "", "", ""]
		dayFourArray = ["", "", "", "", "", ""]
		dayFiveArray = ["", "", "", "", "", ""]
		dayOneArray[0], dayOneArray[1], dayOneArray[2], dayOneArray[3], dayOneArray[4], dayOneArray[5] = getDay(dayOne)
		dayTwoArray[0], dayTwoArray[1], dayTwoArray[2], dayTwoArray[3], dayTwoArray[4], dayTwoArray[5] = getDay(dayTwo)
		dayThreeArray[0], dayThreeArray[1], dayThreeArray[2], dayThreeArray[3],dayThreeArray[4], dayThreeArray[5] = getDay(dayThree)
		dayFourArray[0], dayFourArray[1], dayFourArray[2], dayFourArray[3], dayFourArray[4], dayFourArray[5] = getDay(dayFour)
		dayFiveArray[0], dayFiveArray[1], dayFiveArray[2], dayFiveArray[3], dayFiveArray[4], dayFiveArray[5] = getDay(dayFive)

		#format the timetable onto the page, loaded from the day arrays into columns
		periodLabel = ttk.Label(frame1, text="Period 1 :\n"
											"Period 2 :\n"
											"Period 3 :\n"
											"Period 4 :\n"
											"Period 5 :\n"
											"Period 6 :", background='white', font=('Calibri', '14'))
		periodLabel.place(x=70, y=390)
		dayOneLabel = ttk.Label(frame1, text= "Day 1 \n"+\
											  dayOneArray[0] + "\n" + \
											  dayOneArray[1] + "\n" + \
											  dayOneArray[2] + "\n" + \
											  dayOneArray[3] + "\n" + \
											  dayOneArray[4] + "\n" + \
											  dayOneArray[5], background='white', font=('Calibri', '14'))
		dayOneLabel.place(x=190, y=367)
		dayTwoLabel = ttk.Label(frame1, text="Day 2 \n" + \
											 dayTwoArray[0] + "\n" + \
											 dayTwoArray[1] + "\n" + \
											 dayTwoArray[2] + "\n" + \
											 dayTwoArray[3] + "\n" + \
											 dayTwoArray[4] + "\n" + \
											 dayTwoArray[5], background='white', font=('Calibri', '14'))
		dayTwoLabel.place(x=310, y=367)
		dayThreeLabel = ttk.Label(frame1, text="Day 3 \n" + \
											 dayThreeArray[0] + "\n" + \
											 dayThreeArray[1] + "\n" + \
											 dayThreeArray[2] + "\n" + \
											 dayThreeArray[3] + "\n" + \
											 dayThreeArray[4] + "\n" + \
											 dayThreeArray[5], background='white', font=('Calibri', '14'))
		dayThreeLabel.place(x=430, y=367)
		dayFourLabel = ttk.Label(frame1, text="Day 4 \n" + \
											 dayFourArray[0] + "\n" + \
											 dayFourArray[1] + "\n" + \
											 dayFourArray[2] + "\n" + \
											 dayFourArray[3] + "\n" + \
											 dayFourArray[4] + "\n" + \
											 dayFourArray[5], background='white', font=('Calibri', '14'))
		dayFourLabel.place(x=550, y=367)
		dayFiveLabel = ttk.Label(frame1, text="Day 5 \n" + \
											 dayFiveArray[0] + "\n" + \
											 dayFiveArray[1] + "\n" + \
											 dayFiveArray[2] + "\n" + \
											 dayFiveArray[3] + "\n" + \
											 dayFiveArray[4] + "\n" + \
											 dayFiveArray[5], background='white', font=('Calibri', '14'))
		dayFiveLabel.place(x=670, y=367)

	#screen creation
	root = Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width / 2) - (800 / 2)
	y = (screen_height / 2) - (600 / 2)
	root.geometry('%dx%d+%d+%d' % (800, 600, x, y))
	root.title("Classroom Manager")
	root.resizable(width=False, height=False)
	root.configure(background='white')

	s = ttk.Style()  # creation of standard UI style
	s.configure('tabs.TFrame', background='white')

	teacherName, teacherPic, timetableId = getTeacher(teacherId) #request retrieval of teacher info

	# setting up notebook tabs
	notebook = ttk.Notebook(root)
	notebook.pack(fill=X)
	home = ttk.Frame(notebook)
	notebook.add(home, text='Home     ')

	# Frame setup
	frame1 = ttk.Frame(home, style='tabs.TFrame')  # styles added to ensure standard/clean UI
	frame1.config(height=600, width=800)
	frame1.pack()

	# SETUP for Timetable Tab
	# -------------------------------------------------------------------------------------------------------------

	global buttonPressed
	buttonPressed = False

	welcomeLabel = ttk.Label(frame1, text="Welcome, {}!".format(teacherName)
							 , background='white', font=('Calibri', '18'))
	welcomeLabel.place(x=20, y=30)

	timetableTitle = ttk.Label(frame1, text="Timetable", background='white'
							   , font=('Calibri', '20'))
	timetableTitle.place(x=345, y=330)

	time = str(datetime.now())
	timeLabel = ttk.Label(frame1, text="Time of Login: {}".format(time), background='white'
						  , font=('Calibri', '10'))
	timeLabel.place(x=25, y=540)

	logout = ttk.Button(frame1, text="Logout", command=lambda : sysLogout(root))
	logout.place(x=640, y=40)

	global standartT
	standardT = PhotoImage(file=teacherPic)
	#standardT = standardT.subsample(3, 3)  # subsampling done to reduce and configure size of images
	tImageLabel = ttk.Label(frame1, image=standardT)
	tImageLabel.place(x=30, y=60)

	createTimetable(timetableId) #timetable must be loaded from SQLite Database

	global schoolIMG
	schoolIMG = PhotoImage(file='Images/school.gif')
	schoolIMG = schoolIMG.subsample(3, 3)
	schoolLabel = ttk.Label(frame1, image=schoolIMG)
	schoolLabel.place(x=600, y=95)

	classLabel = ttk.Label(frame1, text="Classes: ", background='white', font=('Calibri', '12'))
	classLabel.place(x=280, y=105)
	classList.classButtons(root, frame1, teacherId, notebook)

	root.mainloop() #UI loop

	return buttonPressed #returns if the user has exited the application or logged out for processing in init()