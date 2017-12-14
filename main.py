import sys
class ToDo(object):

    def __init__(self):
        self.my_files = []
        other_file = open("list.py", "r")
        self.lines = other_file.readlines()
        for i in self.lines:
            self.my_files.append(i)

    def __str__(self):
        result = ""
        for i in range(0, len(self.my_files)):
            result += str(i + 1) + ". " + self.my_files[i].__str__() + "\n"
        return result

main = ToDo()

counting = open('list.py','r').readlines()

program_name = sys.argv[0]

arguments = sys.argv[1:]

count = len(arguments)

commands = ['-l','-r','-a','-c']


if len(sys.argv) == 1 or set(commands) - set(sys.argv) ==set(commands):
    print('''Command Line Todo application
    =============================

    Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task''')

if len(sys.argv) == 2:
    if sys.argv[-1] == '-l':
        print(main)
        if len(main.lines) == 0:
            print('NOPE')
    if sys.argv[-1] == '-a':
        print('no task defined')
    if sys.argv[-1] == '-r':
        print('no index provided')

# #     def complete(self):
#         self.completed = True

#     def __str__(self):
#         return ("[x] " if self.completed else "[ ] ") + self.name

if len(sys.argv) == 3:
    if sys.argv[-2] == '-a':
        with open('list.py', 'a') as file:
            file.writelines('[ ]' + sys.argv[-1] +'\n')
    
    if sys.argv[-2] == '-r':
        if sys.argv[-1].isnumeric():
            if int(sys.argv[-1]) > len(counting):
                print('out of range')
            if int(sys.argv[-1]) <= len(counting):
                infile = open('list.py','r').readlines()
                with open('list.py','w') as outfile:
                    for index,line in enumerate(infile):
                        if index != (int(sys.argv[-1]))-1:
                            outfile.write(line)
        else:
            print('write a number')

    if sys.argv[-2] == '-c':
        infile = open('list.py','r').readlines()
        with open('list.py','w') as outfile:
            for index,line in enumerate(infile):
                if index != (int(sys.argv[-1]))-1:
                    outfile.write(line)
                if index == (int(sys.argv[-1]))-1:
                    outfile.write(str(line).replace('[ ]', '[x]'))



