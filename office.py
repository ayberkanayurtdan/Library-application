def courseInfos(choose):             #this function reads course.txt and returns all infos with using parameter.
    coursetxt=open("course.txt","r")
    courseinfos=coursetxt.readlines()
    coursetxt.close()

    courseCodes=[]
    courseNames=[]
    authors=[]
    countCourses=[]

    for course in courseinfos:
        course=course.strip("\n")
        courseDatas=course.split(";")
        courseCode=courseDatas[0]
        courseCodes.append(courseCode)
        courseName=courseDatas[1]
        courseNames.append(courseName)
        author=courseDatas[2]
        authors.append(author)
        countCourse=int(courseDatas[3])
        countCourses.append(countCourse)
    
    if choose==0:
        return courseCodes
    elif choose==1:
        return courseNames
    elif choose==2:
        return authors
    elif choose==3:
        return countCourses

def studentInfos(choose):            #this function reads student.txt and returns all infos with using parameter.
    studenttxt=open("student.txt","r",encoding="utf-8")
    studentinfos=studenttxt.readlines()
    studenttxt.close()

    studentIds=[]
    studentNames=[]
    studentCourses=[]

    for student in studentinfos:
        student=student.strip("\n")
        studentData=student.split(";")
        studentid=int(studentData[0])
        studentIds.append(studentid)
        studentname=studentData[1]
        studentNames.append(studentname)
        studentCourse=studentData[2]
        studentCourses.append(studentCourse)

    if choose==0:
        return studentIds
    elif choose==1:
        return studentNames
    elif choose==2:
        return studentCourses

def courses():
    print(courseInfos(1)) 

def takenCourses():
    takenCourses=[]
    courseName=courseInfos(1)
    countCourse=courseInfos(3)
    for counter in range(0,len(countCourse)):                               #if no one register this course "countCourse" will be 0.
        if countCourse[counter]!=0:                                         #if it's 0 then the loop doesn't print it
            takenCourses.append(courseName[counter])
    print(takenCourses)

def addCourse():
    courseCodes=courseInfos(0)
    code=input("Please enter the course code that you want to add: ")

    if len(code)!=8:                                                        #Course code must be 8 digit
        print("Course code must be 8 digit. You are being redirected to the home page.")
        return "this line stops the function"
    for index in range(0,len(courseCodes)):                                 #If code is already exist you can't write again this code
        if code==courseCodes[index]:
            print("This code already exists.You are being redirected to the home page.")
            return "this line stops the function"

    name=input("Please enter the course name that you want to add: ")
    author=input("Please enter the author that you want to add: ")
    
    coursetxt=open("course.txt","a")                                        #this code adds the course to 'course.txt'
    coursetxt.write("\n"+code+";"+name+";"+author+";"+"0")
    coursetxt.close()

    print( "Mission complete!")

def searchCourseByCode():
    code=input("Please enter the course code that you want to search: ")
    courseCodes=courseInfos(0)
    courseNames=courseInfos(1)
    for index in range(0,len(courseCodes)):
        if code==courseCodes[index]:                #If the code that the user input is the same as the course code then it prints the course code.
            print(courseNames[index])
            return "this line stops the function"

    print("There is no such course code.")        #If course code isn't in txt then it prints this warning.

def searchCourseByName():
    courseNames=courseInfos(1)
    counter=0
    name=input("Please enter the course name that you want to search:")
    for index in range(0,len(courseNames)):
        if name in courseNames[index]:
            print(courseNames[index])
            counter+=1
    if counter==0:
        print("No such course was found.")      ##If course name isn't in txt then it prints this warning.

def giveCourse():
    studentIds=studentInfos(0)
    studentNames=studentInfos(1)
    studentCourses=studentInfos(2)

    courseCodes=courseInfos(0)
    courseNames=courseInfos(1)
    author=courseInfos(2)
    countCourses=courseInfos(3)

    studentinfos=[]
    courseinfos=[]

    warning=1

    id=int(input("Please enter the student id: "))
    
    for index1 in range(0,len(studentIds)):
        if id==studentIds[index1]:
            warning=-1
            code=input("Please enter the course code: ")
            for index2 in range(0,len(courseCodes)):
                if code==courseCodes[index2]:
                    warning=0                                                   #if student id and course code are true then warning is 0
                    studentCourses[index1]=studentCourses[index1]+","+code      #this line updates the student's courses
                    countCourses[index2]+=1                                     #this line updates the number of courses taken
        
    if warning==1:                  #if student id is wrong, 'warning' is 1 
        print("There is no such student number. You are being redirected to the home page. ")
        return "this line stops the function"

    if warning==-1:                 #if student id is true but course code is wrong, 'warning is -1
        print("There is no such course code. You are being redirected to the home page. ")
        return "this line stops the function"


    for counter in range(len(studentIds)):              #this line uptadets 'studentinfos'
        if counter!=len(studentIds)-1:
            studentinfos.append(str(studentIds[counter])+";"+studentNames[counter]+";"+studentCourses[counter]+"\n")
        else:
            studentinfos.append(str(studentIds[counter])+";"+studentNames[counter]+";"+studentCourses[counter])

    for counter in range(len(courseCodes)):             #this line uptades 'courseinfos'
        if counter!=len(courseCodes)-1:
            courseinfos.append(courseCodes[counter]+";"+courseNames[counter]+";"+author[counter]+";"+str(countCourses[counter])+"\n")
        else:
            courseinfos.append(courseCodes[counter]+";"+courseNames[counter]+";"+author[counter]+";"+str(countCourses[counter]))
    
    studenttxt=open("student.txt","r+", encoding="utf-8")
    studenttxt.seek(0)
    studenttxt.writelines(studentinfos)                 #overwrite 'studentinfos' to 'student.txt'

    coursetxt=open("course.txt","r+")                   #overwrite 'courseinfos' to 'course.txt'
    coursetxt.seek(0)
    coursetxt.writelines(courseinfos)

    studenttxt.close()
    coursetxt.close()

    print("Mission complete!")

def students():
    studentNames=studentInfos(1)
    studentCourses=studentInfos(2)

    for index in range(0,len(studentNames)):
        print(str(index+1)+"-"+studentNames[index]+":"+"\n"+studentCourses[index])      #it prints student name and switch the next line then it prints course codes that students registered.        

def crowdedCourses():
    countCourses=courseInfos(3)
    courseNames=courseInfos(1)
    crowdedCourseList=[]
    sort=0      #it's just an arrangement (like '1'-asd     '2'-das ) 

    for repeat in range(0,3):
        max=0
        name=""
        sort+=1                     # '1' and '2' and '3'
        deleting=0
        for index in range(0,len(countCourses)):
            if countCourses[index]>max:             #it finds maximum registered course
                max=countCourses[index]
                name=courseNames[index]
                deleting=index
        crowdedCourseList.append(str(sort)+"-"+name+":"+str(max))   #this line updates the 'crowdedCourseList'
        courseNames.remove(courseNames[deleting])                   #we are delete this two things because when we find max
        countCourses.remove(countCourses[deleting])                 #we need second and third maximum value then we remove maximum values

    
    for index in range(0,3):
        print(crowdedCourseList[index])                             

def mostCourseStudent():
    studentNames=studentInfos(1)
    studentCourses=studentInfos(2)

    mostCourseStudentList=[]
    sort=0
    
    for repeat in range(0,3):
        max=0
        name=""
        deleting=0
        sort+=1
        for index in range(0,len(studentCourses)):      #this for loop finds max value
            count=1
            if studentCourses[index]=='':               #if there is no course then count is 0.
                count=0
            for x in studentCourses[index]:
                if x==",":                              #we split the courses using ',' so if there is any ',' then there is 1 course if we use ',' then it's increasing one by one
                    count+=1
            if count>max:
                name=studentNames[index]
                deleting=index
                max=count
        mostCourseStudentList.append(str(sort)+"-"+name+":"+str(max))               #we find max value and add to 'mostCourseStudentList' with its infos
        studentNames.remove(studentNames[deleting])                                 
        studentCourses.remove(studentCourses[deleting])                             ##we delete the max values for find second and third values

    for index in range(0,3):
        print(mostCourseStudentList[index])

def main_menu():                #it's main menu. We use terminal for do things that users request
    print("\n 1-List all the courses. \n 2-List all the course that have at least one student registered. \n 3-Add a new course. \n 4-Search a course by course code \n 5-Search a course by name \n 6-Register a student to a course. \n 7-List all the students. \n 8-List top 3 most crowded courses  \n 9-List top 3 students with the most course registrations  \n q-Exit. ")
    choose=input("Please select the action you want to take: ")
    
    if choose=="1":
        courses()
    elif choose=="2":
        takenCourses()
    elif choose=="3":
        addCourse()
    elif choose=="4":
        searchCourseByCode()
    elif choose=="5":
        searchCourseByName()
    elif choose=="6":
        giveCourse()
    elif choose=="7":
        students()
    elif choose=="8":
        crowdedCourses()
    elif choose=="9":
        mostCourseStudent()
    elif choose=="q":                                         #it's for stopping the infinite loop
        return False
    else:
        print("You have entered a command that does not exist. Please try again")

while True:                     #infinite loop (if we don't write 'q' )
    if main_menu()==False:
        break