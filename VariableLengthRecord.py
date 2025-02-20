class Course:
    def __init__(self, c, tt, type, cd_hr=0, sms=0):
        self.code = c
        self.title = tt
        self.type = type
        self.credit_hrs = cd_hr
        self.semester = sms
    def __str__(self):
        return f'{self.code},{self.title},{self.credit_hrs},{self.type},{self.semester}'

courses = [Course('00000000', 'Object Oriented Programming', 'core', 3, 2),
           Course('00000001', 'Digital Logic Design', 'elective', 3, 2),
           Course('00000011', 'Math Deficiency', 'core', 3, 2),
           Course('00000111', 'Applied Physics', 'core', 3, 2)]
s=f'CODE,TITLE,CREDIT_HOURS,TYPE,SEMESTER\n'
with open('VariableLengthRecords.txt', 'w') as file:
    file.write(str(s)+'\n')
    for i in courses:
        file.write(str(i) + '\n')

menu = 'a) Add\ns) Search\nd) Delete\nl) List All\ne) Edit\nq) Quit'
while True:
    choice = input('Enter your choice: ')
    if choice == 'a':                                             # Add a new course
        c = Course(input('Enter code: '), input('Enter title: '), input('Enter type: '), int(input('Enter credit_hrs: ')), int(input('Enter semester: ')))
        courses.append(c)
        with open('VariableLengthRecords.txt', 'a') as file:
            file.write(str(c) + '\n')
    elif choice == 's':                                           # Search for a course
        code = input('Enter the code you want to search: ')
        found = False
        with open('VariableLengthRecords.txt', 'r') as file:
            for line in file:
                if line.split(',')[0] == code:
                    print(line)
                    found = True
                    break
        if not found:
            print("Course not found.")
    elif choice == 'd':                                          # Delete a course
        code = input('Enter the code you want to delete: ')
        with open('VariableLengthRecords.txt', 'r') as file:
            lines = file.readlines()
        with open('VariableLengthRecords.txt', 'w') as file:
            for line in lines:
                if line.split(',')[0]!=code:
                    file.write(line)
                else:
                    file.write('???'+line)  
    elif choice=='l':                                            #list all courses
        with open('VariableLengthRecords.txt', 'r') as file:
            for line in file:
                print(line)  
    elif choice == 'e':                                          # Edit a course
        code = input('Enter the code you want to edit: ')
        with open('VariableLengthRecords.txt', 'r') as file:
            lines = file.readlines()
        with open('VariableLengthRecords.txt', 'w') as file:
            for line in lines:
                if line.split(',')[0] == code:
                    c = Course(input('Enter new code: '), input('Enter new title: '), input('Enter new type: '), int(input('Enter new credit_hrs: ')), int(input('Enter new semester: ')))
                    file.write(str(c) + '\n')
                else:
                    file.write(line)
    elif choice == 'q':                                          # quit
        break
    else:
        print(f'Invalid input\nChoose from the following:\n{menu}')






         
        
        