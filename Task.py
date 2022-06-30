import subprocess as sp
from datetime import datetime
from bash import *

class Task(object):
    def __init__(self, task=None):
        self._task = task
        self.lastReturnCode = 0
        self.lastStdout = ''
        self.lastStderr = ''

    def version(self):
        output = self.run(['-v'])
        return output.stdout.strip()

    def run(self, argv):
        if self._task == None:
            return
        output = sp.run([self._task] + argv, capture_output=True, text=True)
        
        self.recordTask(output)
        return output.returncode == 0

    def existCode(self):
        return self._lastReturnCode

    def recordTask(self, output):
        self.lastReturnCode = output.returncode
        self.lastStdout = output.stdout
        self.lastStderr = output.stderr

    def log(self, log_stderr=True, log_stdout=False):
        if self.lastReturnCode == 0:
            return
        logName = f'{self._task}_{datetime.now().strftime("%Y_%m_%d_%H%M%S")}.log'
        f = open(logName, "w")
        f.write(self.lastStderr)
        f.close()
        return logName 

    def taskName(self):
        name = self._task
        return name
    def __str__(self):
        return self._task
