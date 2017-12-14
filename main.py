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
        result = "\n\n"
        for i in range(0, len(self.my_files)):
            result += str(i + 1) + ". " + self.my_files[i].__str__() + "\n"
        return result

main = ToDo()

counting = open(str(absolute_path),'r').readlines()

commands = ['-l','-r','-a','-c','-la','-rc','-ar']

display = '''\n
    ______________________________
    commandline ideaflow
                               <&>


         -l    Lists all the tasks
         -a    Adds a new task
         -r    Removes an task
         -c    Completes an task
  
         -la   Lists the unchecked
               tasks only
         -rc   Removes all checked
               tasks
         -ar   At given index
               task is rewritten
    \n'''

if len(sys.argv) == 1:
    print(display)
    
if set(commands) - set(sys.argv) == set(commands) and len(sys.argv) > 1:
    print('\ninvalid argument or syntax' + display)


if len(sys.argv) == 2:

    if sys.argv[-1] == '-l':
        print(main)
        if len(main.lines) == 0:
            print('\nNONE')
    if sys.argv[-1] == '-la':
        print('\nlisting unfinished tasks only\n')
        for i in range(len(main.my_files)):
            if main.my_files[i][1] == ' ':
                print(main.my_files[i])
        if len(main.lines) == 0:
            print('\nNONE')
    if sys.argv[-1] == '-rc':
        infile = open(str(absolute_path),'r').readlines()
        with open(str(absolute_path),'w') as outfile:
            for line in infile:
                if str(line[1]) is 'x':
                    pass
                else:
                    outfile.write(line)
        print('\nremoved all finished tasks')
    if sys.argv[-1] == '-a':
        print('\nno task defined')
    if sys.argv[-1] == '-r':
        print('\nno index provided')
    if sys.argv[-1] == '-c':
        print('\nno index provided')

if len(sys.argv) == 3:

    if sys.argv[-2] == '-a':
        with open(str(absolute_path), 'a') as file:
            file.writelines('[ ]' + sys.argv[-1] +'\n')
            print('\nadded new task')
    
    if sys.argv[-2] == '-r':
        if sys.argv[-1].isnumeric():
            if int(sys.argv[-1]) > len(counting):
                print('\nout of range')
            if int(sys.argv[-1]) <= len(counting):
                infile = open(str(absolute_path),'r').readlines()
                with open(str(absolute_path),'w') as outfile:
                    for index,line in enumerate(infile):
                        if index != (int(sys.argv[-1]))-1:
                            outfile.write(line)
                print('\nremoved task at index ' + str(sys.argv[-1]))
        else:
            print('\nwrite a number')

    if sys.argv[-2] == '-c':
        if sys.argv[-1].isnumeric():
            if int(sys.argv[-1]) > len(counting):
                print('\nout of range')
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
                print('\ncompleted a task at index ' + str(sys.argv[-1]))
        else:
            print('\nwrite a number')

if len(sys.argv) == 4:

    if sys.argv[-3] == '-a':
        with open(str(absolute_path), 'a') as file:
            file.writelines('[ ]' + sys.argv[-2] +'\n')
            file.writelines('[ ]' + sys.argv[-1] +'\n')
            print('\nadded two new tasks')

    if sys.argv[-3] == '-ar':
        infile = open(str(absolute_path),'r').readlines()
        with open(str(absolute_path),'w') as outfile:
            for index,line in enumerate(infile):
                if index == (int(sys.argv[-2]))-1:
                    outfile.write('[ ]' + sys.argv[-1] +'\n')
                else:
                    outfile.write(str(line))
        print('\nrewritten task at index ' + str(sys.argv[-2]))