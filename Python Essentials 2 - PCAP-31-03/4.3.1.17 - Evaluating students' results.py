from os import strerror, getcwd

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __str__(self):
        return 'Bad data in file.'

class FileEmpty(StudentsDataException):
    def __str__(self):
        return 'File is empty.'



matrix = {}
cwd = getcwd()
srcname = input("Enter the source file name: ")
try:
    src = open(cwd + "/Python Class 2/" + srcname, 'r')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    print(cwd + "/" + srcname)
    exit(e.errno)

try:
    currline = src.readline()
    if currline == '':
        raise FileEmpty
except FileEmpty as fe:
    print("Exception raised:", fe)
else:
    try:
        while currline != '':
            try:
                first_name = currline[0:7].strip()
                last_name = currline[8:15].strip()
                score = float(currline[16:])
            except IndexError as ie:
                print ("Error on line:", currline)
                print(ie)
                raise BadLine
            except ValueError as ve:
                print ("Error on line:", currline)
                print(ve)
                raise BadLine
            else:
                full_name = first_name + " " + last_name
                if full_name in matrix:
                    matrix[full_name] = matrix[full_name] + score
                else:
                    matrix[full_name] = score
            currline = src.readline()

        sorted_matrix = dict(sorted(matrix.items(),key=lambda x:x[0]))
    
        for student in sorted_matrix:
            print(student.ljust(16,' '), sorted_matrix[student])

    except BadLine as bl:
        print("Exception raised:", bl)
    finally:
        src.close()