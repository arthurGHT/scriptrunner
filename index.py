from bash import *
from Task import Task
import sys
import json



def loadScript(file):
    f = open(file)
    return json.load(f)


if __name__ == '__main__':
    base_directory = pwd()
    script = loadScript(sys.argv[1])
    tools = []
    for i in script['tools']:
        tools.append(Task(i))

    for step in script['step']:
        if step['taskName'] == "cd":
            cd(step['directory'])
        elif step['taskName'] == "rm":
            rm(step['file'])
        else:
            taskname = step ['taskName']
            print(f'Running: {taskname}', end='\r')
            tool = tools[step['toolIndex']]
            if not tool.run(step['script'].split()[1:]):
                errorLog(tool, base_directory)
            print('                                                ', end='\r')
            print(' \u2705 ' + taskname)
