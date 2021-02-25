from dataclasses import dataclass
from typing import List

from practice import CompiledFile


@dataclass
class Server:
    workQueue: List
    cache: set
    currentTask: CompiledFile

    def work(self):
        if(self.currentTask == None):
            self.currentTask = self.workQueue.pop()
        else:
            self.currentTask.compile_time -= 1 # do one unit of work

            if(self.currentTask.compile_time == 0):# if this task is done
                self.cache.add(self.currentTask.name) # add to cache
                self.currentTask = None