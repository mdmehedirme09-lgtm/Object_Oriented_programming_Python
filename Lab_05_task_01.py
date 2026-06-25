class Students_GPA():
    def __init__(self):
        # self.name=name
        # self.gpa=gpa

        students={}
        while True:
            name=input("Enter student name: ")
            gpa=input("Enter student GPA: ")
            students[name]=gpa
            choice=input("Do you want to enter another record? Press 'y' if yes: ")
            if choice.lower() != 'y':
                break
        print(students)
st=Students_GPA()
