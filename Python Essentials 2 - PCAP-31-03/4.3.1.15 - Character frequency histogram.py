from os import strerror, getcwd

matrix = {}
cwd = getcwd()
srcname = input("Enter the source file name: ")
try:
    src = open(cwd + "/Python Class 2/" + srcname, 'r')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    print(cwd + "/" + srcname)
    exit(e.errno)

curr = src.read(1)
while curr != '':
    if curr.isalpha():
        if curr in matrix:
            matrix[curr] = matrix[curr] + 1
        else:
            matrix[curr] = 1
    curr = src.read(1)

src.close()

for item in matrix:
    if matrix[item] > 0:
        print(item, "->", matrix[item])