import sqlite3
"""
Key format:
  - Action -> Data -> parameters
  - Action to what data based on which parameters
     - i.e. request the teacherId based on username from the database is: 
       requestTeacherId_username
"""

#Login
def requestTeacherId_username(userName): #retrieve teacherId based on username
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT teacherId FROM teacher WHERE teacher.username='{}'".format(userName))
	teacherId = c.fetchone()[0]
	conn.close()
	return teacherId

def requestTeacherId_passwordTeacher(password, teacher): #retrieve teacherId based on password and teacherId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT teacherId FROM teacher WHERE teacher.password='{}' AND teacher.teacherId='{}'"
			  .format(password, teacher))
	teacherId = c.fetchone()[0]
	conn.close()
	return teacherId

#Main
def requestTeacher_teacherId(teacherId): #retrieve teacher info for main program based on teacherId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT * FROM teacher WHERE teacher.teacherId='{}'".format(teacherId))
	(id, name, username, password, pic, timetableId) = c.fetchall()[0]
	conn.close()
	return name, pic, timetableId

def requestTimetable_timetableId(timetableId): #retrieve the dayIds for loading into the timetable
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT * FROM timetable WHERE timetable.timetableId='{}'".format(timetableId))
	(timetableId, dayOne, dayTwo, dayThree, dayFour, dayFive) = c.fetchall()[0]
	conn.close()
	return timetableId, dayOne, dayTwo, dayThree, dayFour, dayFive

def requestDay_day(day): #retrieve the periods of the day based on dayId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	dayArray = ["", "", "", "", "", ""]  # preloaded for 6 periods of day timetable
	c.execute("SELECT * FROM day WHERE day.dayId='{}'".format(day))
	(dayId, dayArray[0], dayArray[1],
	 dayArray[2], dayArray[3], dayArray[4], dayArray[5]) = c.fetchall()[0]
	conn.close()
	return dayArray[0], dayArray[1], dayArray[2], dayArray[3], dayArray[4], dayArray[5]

#ClassList
def requestNumClasses_teacherId(teacherId): #retrieve number of classes for the individual teacher
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT className FROM class WHERE class.classTeacher='{}'".format(teacherId))
	numClasses = len(c.fetchall())
	conn.close()
	return numClasses

def requestClass_teacherId(teacherId, i): #retrieve i'th class for the teacher
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT * FROM class WHERE class.classTeacher='{}'".format(teacherId))
	classArray = c.fetchall()[i]
	conn.close()
	return classArray

#ClassTab
def requestNumStudents_classArray(classArray): #retrieve number of students in a particular class
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT studentId FROM studentClass WHERE studentClass.classId='{}'".format(classArray))
	numStudents = len(c.fetchall())
	conn.close()
	return numStudents

def requestStudentClass_classArray(classArray, i): #retrieve the i'th student of the class
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT * FROM studentClass WHERE studentClass.classId='{}'".format(classArray))
	student = c.fetchall()[i]
	conn.close()
	return student

#StudentFunction
def requestStudent_studentId(studentId): #retrieve student info based on studentId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT * FROM student WHERE student.studentId='{}'".format(studentId))
	(studentId, studentName) = c.fetchall()[0]
	conn.close()
	return studentId, studentName

def updateStudentMark_studentClassIdTaskNumMark(studentClassId, assignmentId, mark):
	#update the student mark of a student in the class for a particular assignment to the mark passed in
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("UPDATE studentClassAssignment SET Mark='{}' WHERE studentClassAssignment.studentClassId='{}' AND"
			  " studentClassAssignment.assignmentId='{}'".format(mark, studentClassId, assignmentId))
	conn.commit()
	conn.close()
	# feedback for database managers / administrators (not for user)
	print("updated the studentClass {} on assignment {} to a mark of {}".format(studentClassId, assignmentId, mark))
	return

def updateStudentClassBehaviour_studentClassId(note, studentClassId):
	#update the student's behaviour note in a class to the note passed in as 'note'
	if (len(note)) < 1000: #to prevent overloading of system 1000 character max limit is set
		conn = sqlite3.connect('major.db')
		c = conn.cursor()
		c.execute("UPDATE studentClassBehaviourNote SET Note='{}' WHERE studentClassBehaviourNote.studentClassId='{}'"
				  .format(note, studentClassId))
		conn.commit()
		conn.close()
		# feedback for database managers / administrators (not for user)
		print("Saved note to studentClassId {}".format(studentClassId))
		done = True
	else:
		done = False
	return done

def requestNote_studentClassId(studentClassId): #retrieve behaviour note for student in class from studentClassId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT Note FROM studentClassBehaviourNote WHERE studentClassBehaviourNote.studentClassId='{}'"
			  .format(studentClassId))
	students = c.fetchall()
	conn.close()
	return students

#AssignmentAdd
def requestStudentInClass_classId(classId): #retrieve students in class based on classId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT studentClassId FROM studentClass WHERE studentClass.classId='{}'".format(classId))
	students = c.fetchall()
	conn.close()
	return students

def requestTaskNum_classId(classId): #retrieve the last task's number based on classId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT taskNum FROM assignment WHERE assignment.classId='{}'".format(classId))
	assNo = (len(c.fetchall()))
	conn.close()
	return assNo

def requestAssignmentId_classIdTaskNum(classId, taskNum): #retrieve assignmentId based on the taskNum of classId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT assignmentId FROM assignment WHERE assignment.classId='{}' AND assignment.taskNum='{}'"
			  .format(classId, taskNum))
	assignmentId = c.fetchall()[0]
	conn.close()
	return assignmentId

def addAssignment_classIdTaskNum(classId, taskNum): #add an assignment for class classId with a task number of taskNum
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("INSERT INTO assignment(classId, taskNum) VALUES ('{}', '{}')".format(classId, taskNum))
	conn.commit()
	conn.close()
	# feedback for database managers / administrators (not for user)
	print("Created an assignment with values {} and {}".format(classId, taskNum))
	return

def addStudentClassAssignment_studentClassIdAssignmentId(studentClassId, assignmentId):
	#add the assignment to each student in the class by creating a studentClassAssignment row with passed in data
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("INSERT INTO studentClassAssignment(studentClassId, assignmentId) VALUES ('{}', '{}')"
			  .format(studentClassId,assignmentId))
	conn.commit()
	conn.close()
	# feedback for database managers / administrators (not for user)
	print("Created a student class assignment with the values {} and {}".format(studentClassId, assignmentId))
	return

def requestStudentClassAssignmentMark_studentClassIdAssignmentId(studentClassId, assignmentId):
	#retrieve the assignment mark for the student in the class
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("SELECT Mark FROM studentClassAssignment WHERE studentClassAssignment.studentClassId='{}' AND "
			  "studentClassAssignment.assignmentId='{}'".format(studentClassId, assignmentId))
	mark = c.fetchall()[0]
	conn.close()
	return mark

def subStudentClassAssignment_studentClassIdAssignmentId(studentClassId, assignmentId):
	#subtract / remove the studentClassAssignments with based on studentClassId and assignmentId
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("DELETE FROM studentClassAssignment WHERE studentClassAssignment.studentClassId='{}' "
			  "AND studentClassAssignment.assignmentId='{}'".format(studentClassId, assignmentId))
	conn.commit()
	conn.close()
	# feedback for database managers / administrators (not for user)
	print("Deleted row where studentClassId is {} for assignmentId {}".format(studentClassId, assignmentId))
	return

def subAssignment_AssignmentId(assignmentId):
	#subtract / remove an assignment with assignmentId passed in
	conn = sqlite3.connect('major.db')
	c = conn.cursor()
	c.execute("DELETE FROM assignment WHERE assignment.assignmentId='{}'".format(assignmentId))
	conn.commit()
	conn.close()
	# feedback for database managers / administrators (not for user)
	print("Deleted assignmentId {}".format(assignmentId))
	return
