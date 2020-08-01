#imports
from tkinter import *
from tkinter import ttk
import sys
import database

"""
Change to return a reason and compare all facets of the login including username and password
"""

#login takes password passed in from main program
def login():
	def setup():
		#setup root window
		global rootLog
		rootLog = Tk()
		screen_width = rootLog.winfo_screenwidth()
		screen_height = rootLog.winfo_screenheight()
		x = (screen_width/2) - (300/2)
		y = (screen_height/2) - (200/2)
		rootLog.geometry('%dx%d+%d+%d' % (300, 200, x, y))
		rootLog.protocol('WM_DELETE_WINDOW', submitEX) #safely exits the application without errors

		rootLog.title("User Login")
		rootLog.resizable(width=False, height=False)
		rootLog.configure(background='white')

		#setup onscreen widgets
		spaceLabel = ttk.Label(rootLog, text="", background='white')
		spaceLabel.grid(row=1, column=0, padx=55)

		loginLabel = ttk.Label(rootLog, text="Enter Username:", background='white')
		loginLabel.grid(row=2, column=0, pady=10, padx=25)

		global uN #username entry field i.e. uN
		uN = ttk.Entry(rootLog, width=25)
		uN.grid(row=3, column=0, padx=75)

		passwordLabel = ttk.Label(rootLog, text="Enter Password:", background='white')
		passwordLabel.grid(row=4, column=0, pady=5, padx=25)

		global uP #user password entry field i.e. uP
		uP = ttk.Entry(rootLog, show="*",width=25)
		uP.grid(row=5, column=0, padx=75)

		submit_button = ttk.Button(rootLog, text="LOGIN", command=submitUN)
		submit_button.grid(row=6, column=0, pady=10)

		rootLog.mainloop()

	def submitUN():
		#get variables from entry widgets
		global userName
		userName = uN.get()
		global userPass
		userPass = uP.get()
		rootLog.destroy()
		verify()

	def submitEX():
		#error free method of exiting instead of just destroying the root
		sys.exit("Exited Application")

	def verify():
		global valid #valid is true if the login is successful
		global teacherId
		try: #try except implemented as if the match failed NoneType objects aren't subscriptable
			teacherId1 = database.requestTeacherId_username(userName)
			teacherId2 = database.requestTeacherId_passwordTeacher(userPass, teacherId1)
			if teacherId1 == teacherId2: #correct username and password ids match
				valid = True
				teacherId = teacherId1
			else:
				valid = False
		except:
			valid = False
	global valid
	valid = False
	global teacherId

	teacherId = 0
	setup() #sets up popup module

	#pass parameters back to main program
	return valid, teacherId