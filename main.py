import sys

initial = sys.argv
absolute_path = r"C:\Users\Andras\greenfox\my_todo\nyarai_andras_todo\list.py"

class Application(object):

    def __init__(self):
        self.my_files = []
        list_file = open(str(absolute_path), "r")
        self.lines = list_file.readlines()
        for i in self.lines:
            self.my_files.append(i)
        list_file.close()

    def collapse(self):
        return ' '.join(initial[2:])

    def add(self, iterable):
        with open(str(absolute_path), 'a') as file:
            file.writelines('[ ] ' + iterable +'\n')

    def remove(self, target_index):
        infile = open(str(absolute_path),'r').readlines()
        with open(str(absolute_path),'w') as outfile:
            for index,line in enumerate(infile):
                if index != (int(target_index))-1:
                    outfile.write(line)
    
    def complete(self, target_index):
        infile = open(str(absolute_path),'r').readlines()
        with open(str(absolute_path),'w') as outfile:
            for index,line in enumerate(infile):
                if index != (int(target_index))-1:
                    outfile.write(line)
                if index == (int(target_index))-1:
                    if str(line[1]) is ' ':
                        outfile.write(str(line).replace('[ ] ', '[x] ', 1))
                    else:
                        outfile.write(str(line))

    def compare(self):
        return len(self.my_files)

    def __str__(self):
        if len(self.my_files) == 0:
            return "\n\nNO ITEM"
        result = "\n\n"
        for i in range(0, len(self.my_files)):
            result += str(i + 1) + ". " + self.my_files[i].__str__() + "\n"
        return result

    def display(self):
        return '''\n
    ______________________________
    commandline ideaflow
                               <&>

         -l    listing current
         -a    adds new item
         -r    removes item
         -c    complete item
  
                 '''+ "/" + str(len(self.my_files)) + '''
    \n'''
        
obj = Application()

if len(initial) == 1:
    print(obj.display())
if len(initial) == 2:
    if initial[1] == '-l':
        print(obj)
    if initial[1] == '-a':
        print('\nno task defined')
    if initial[1] == '-r' or initial[1] == '-c':
        print('\nno index provided')
if len(initial) >= 3:
    initial[2] = obj.collapse()
    if initial[1] == '-a':
        obj.add(initial[2])
        print('\nadded new task')
    if initial[1] == '-r' or initial[1] == '-c':
        if initial[2].isnumeric():
            if int(initial[2]) > obj.compare():
                print('\nout of range')
            if initial[1] == '-r':
                obj.remove(initial[2])
                print('\nremoved task at index ' + str(initial[2]))
            if initial[1] == '-c':
                obj.complete(initial[2])
                print('\ncompleted a task at index ' + str(initial[2]))
        else:
            print('\nwrite a number')
