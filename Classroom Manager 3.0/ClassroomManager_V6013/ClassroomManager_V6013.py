"""
This application is a classroom manager programmed
by Harrison Crowe-Maxwell.
Developed between 27/04/18 and 28/06/18 under
St Pius X College Major Project Requirements.
Programmed following provided required functionality:

	This program allows a teacher to manage the day
	to day classroom tasks which includes -
		- Class lists in the form of the class pages
		- Recording of marks connected to a database
		    - Marks apply to assignments that can be added
		      and removed as the user sees neccesary
		- Recording of timetable which has been recorded
		  to be viewed on the main tab
		- Behaviour notes for each student can be added
"""

#initialising imports
from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog
import sys
import os
import fail            #...for all modules, see root folder
import main
import log
try: #Try except must be in all PIL calls
	from PIL import * #if the user hasn't installed PIL it is internally interfaced into cmd
except:
	os.popen('pip install Pillow')


#function for program execution
def init():
	valid, teacherId = log.login() #logs into system
	if valid == True:
		logBack = main.mainP(teacherId) #runs main program
		if logBack == True: #logback is only executed if the user 'Logs out'
			incorrect()
		else:
			return
	else:
		fail.fail("Incorrect Username or Password") #incorrect login details
		incorrect()


#if an incorrect password is entered incorrect() is called
def incorrect():
    init() #relaunches the login application process, resets variables

init() #starts login process on application execution
