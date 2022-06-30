import sys
import os
import shutil

def programQuite(msg='', retrunCode=0):
    if len(msg) != 0:
        sys.stderr.write(msg + '\n')
    os._exit(retrunCode)

def fileExist(path):
    if not os.path.exists(path):
        return False
    return os.path.isfile(path)

def dirExist(path):
    if not os.path.exists(path):
        return False
    return os.path.isdir(path)

def pwd():
    return os.getcwd()

def cd(path):
    if not dirExist(path):
        programQuite(path + " is not a directory or not exists", 1)
    os.chdir(path)

def rm(path):
    if dirExist(path):
        shutil.rmtree(path)
    if fileExist(path):
        os.remove(path)

def errorLog(task, base_directory):
    cd(base_directory)
    logName = task.log()
    msg = f'{task.taskName()} with exit code {task.lastReturnCode}\n'
    msg += 'See full log in ' + logName
    programQuite(msg, task.lastReturnCode)