import database
import fail

def addAssignment(classArray): #adds an assignment to the class (classArray)
	students = database.requestStudentInClass_classId(classArray[0]) #gets studentClassIds in class

	assNo = 0
	assNo = (database.requestTaskNum_classId(classArray[0]))+1 #next assessment = num of previous assessments + 1

	if assNo < 13: #limit of 12 assignment per class (to prevent database overloading from spam "+" clicking)
		database.addAssignment_classIdTaskNum(classArray[0], assNo)

		assignmentId = database.requestAssignmentId_classIdTaskNum(classArray[0], assNo)

		for x in students: #for each student in the class create a studentClassAssignment database entry
			database.addStudentClassAssignment_studentClassIdAssignmentId(x[0], assignmentId[0])
	else:
		fail.fail("Maximum amount of assessments reached") #exception
	return

def subAssignment(classArray): #removes an assignment from the class (classArray)
	try: #try except statement for if there are no assignments left and the remove button is pressed
		students = database.requestStudentInClass_classId(classArray[0])

		assNo = 0
		assNo = database.requestTaskNum_classId(classArray[0])
		assignmentId = database.requestAssignmentId_classIdTaskNum(classArray[0], assNo)

		for x in students: #for students in the class remove the assignment in studentClassAssignment
			database.subStudentClassAssignment_studentClassIdAssignmentId(x[0], assignmentId[0])

		database.subAssignment_AssignmentId(assignmentId[0]) #remove the assignment itself from the system
	except:
		return
	return


