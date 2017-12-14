import sys

absolute_path = r"C:\Users\Andras\greenfox\my_todo\nyarai_andras_todo\list.py"

class ToDo(object):

    def __init__(self):
        self.my_files = []
        other_file = open(str(absolute_path), "r")
        self.lines = other_file.readlines()
        for i in self.lines:
            self.my_files.append(i)

    def __str__(self):
        result = ""
        for i in range(0, len(self.my_files)):
            result += str(i + 1) + ". " + self.my_files[i].__str__() + "\n"
        return result

main = ToDo()

counting = open(str(absolute_path),'r').readlines()

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

commands = ['-l','-r','-a','-c','-la','-rc']

if len(sys.argv) == 1 or set(commands) - set(sys.argv) == set(commands):
    print('''\n
    Command Line Todo application
    =============================

    Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task
    
    Optional arguments:
    -la  lists the unchecked
         tasks only
    -rc  removes all checked
         tasks
    \n''')

if len(sys.argv) == 2:
    if sys.argv[-1] == '-l':
        print(main)
        if len(main.lines) == 0:
            print('NOPE')
    if sys.argv[-1] == '-la':
        for i in range(len(main.my_files)):
            if main.my_files[i][1] == ' ':
                print(main.my_files[i])
        if len(main.lines) == 0:
            print('NOPE')
    if sys.argv[-1] == '-rc':
        infile = open(str(absolute_path),'r').readlines()
        with open(str(absolute_path),'w') as outfile:
            for line in infile:
                if str(line[1]) is 'x':
                    pass
                else:
                    outfile.write(line)
    if sys.argv[-1] == '-a':
        print('no task defined')
    if sys.argv[-1] == '-r':
        print('no index provided')
    if sys.argv[-1] == '-c':
        print('no index provided')

if len(sys.argv) == 3:

    if sys.argv[-2] == '-a':
        with open(str(absolute_path), 'a') as file:
            file.writelines('[ ]' + sys.argv[-1] +'\n')
    
    if sys.argv[-2] == '-r':
        if sys.argv[-1].isnumeric():
            if int(sys.argv[-1]) > len(counting):
                print('out of range')
            if int(sys.argv[-1]) <= len(counting):
                infile = open(str(absolute_path),'r').readlines()
                with open(str(absolute_path),'w') as outfile:
                    for index,line in enumerate(infile):
                        if index != (int(sys.argv[-1]))-1:
                            outfile.write(line)
        else:
            print('write a number')

    if sys.argv[-2] == '-c':
        if sys.argv[-1].isnumeric():
            if int(sys.argv[-1]) > len(counting):
                print('out of range')
            if int(sys.argv[-1]) <= len(counting):
                infile = open(str(absolute_path),'r').readlines()
                with open(str(absolute_path),'w') as outfile:
                    for index,line in enumerate(infile):
                        if index != (int(sys.argv[-1]))-1:
                            outfile.write(line)
                        if index == (int(sys.argv[-1]))-1:
                            check = '[ ]'
                            if str(line[1]) is ' ':
                                outfile.write(str(line).replace('[ ]', '[x]', 1))
                            else:
                                outfile.write(str(line))
        else:
            print('write a number')

if len(sys.argv) == 4:

    if sys.argv[-3] == '-a':
        with open(str(absolute_path), 'a') as file:
            file.writelines('[ ]' + sys.argv[-2] +'\n')
            file.writelines('[ ]' + sys.argv[-1] +'\n')


