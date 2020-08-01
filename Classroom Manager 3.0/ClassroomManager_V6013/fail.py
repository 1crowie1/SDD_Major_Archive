#imports
from tkinter import *
from tkinter import ttk


#fail pop-up notification
def fail(why):
    #set up pop-up notification
    global root
    root = Tk() #root initialised as main window with global access
    screen_width = root.winfo_screenwidth() #gets users screen width
    screen_height = root.winfo_screenheight() #gets users screen height
    #position window to appear on users screen in the middle
    x = (screen_width / 2) - (300 / 2)
    y = (screen_height / 2) - (150 / 2)
    root.geometry('%dx%d+%d+%d' % (300, 120, x, y))

    #setup title and basic window details
    root.title("Invalid")
    root.resizable(width=False, height=False)
    root.configure(background='white')

    def submitF(): #ends the root for application restart
        root.destroy()

    #setup the basic UI present in this pop-up window
    failLabel = ttk.Label(root, text="This action is invalid"
                          , background='white')
    failLabel.pack(pady=10)
	#adds reason provided by calling function to invalid login
    noteLabel = ttk.Label(root, text="({})".format(why), background='white')
    noteLabel.pack(pady=5)

    submit_button = ttk.Button(root, text="OK", command=submitF)
    submit_button.pack(pady=10)

    root.mainloop() #UI loop

    return